const http=require('http'),fs=require('fs'),path=require('path'),WebSocket=require('ws');
const PORT=process.env.PORT||3000;
const MIME={'html':'text/html','json':'application/json','png':'image/png','svg':'image/svg+xml','js':'application/javascript','css':'text/css'};
const tank={level_pct:58,volume_L:290,tank_L:500,pump:'OFF',system:'OK',leak:false,unit:'L',calibrated:true,volume_set:true,low_pct:5,high_pct:95,inflow_Lps:0.084,dailyUsage:[42.1,67.3,45,38.2,62.8,20.5,30.1],monthlyUsage:Array.from({length:30},()=>+(20+Math.random()*50).toFixed(1)),fillTarget:null};
const httpServer=http.createServer((req,res)=>{
  let filePath=req.url==='/'?'/index.html':req.url.split('?')[0];
  filePath=path.join(__dirname,filePath);
  fs.readFile(filePath,(err,data)=>{
    if(err){res.writeHead(404);res.end('Not found: '+req.url);return;}
    const ext=path.extname(filePath).slice(1);
    res.writeHead(200,{'Content-Type':MIME[ext]||'text/plain','Cache-Control':'no-cache'});
    res.end(data);
  });
});
const wss=new WebSocket.Server({server:httpServer});
function send(ws,obj){if(ws.readyState===WebSocket.OPEN)ws.send(JSON.stringify(obj));}
function broadcast(obj){wss.clients.forEach(c=>send(c,obj));}
setInterval(()=>{
  if(tank.pump==='FILL'){tank.level_pct=Math.min(tank.level_pct+0.5,100);tank.volume_L=+(tank.level_pct/100*tank.tank_L).toFixed(1);if(tank.level_pct>=tank.high_pct){tank.pump='OFF';broadcast({type:'AUTOSTOP',reason:'high_level',level_pct:tank.level_pct});broadcast({type:'PUMP',state:'OFF'});}if(tank.fillTarget!==null&&tank.level_pct>=tank.fillTarget){const t=tank.fillTarget;tank.pump='OFF';tank.fillTarget=null;broadcast({type:'FILLTO_DONE',target_pct:t,actual_pct:tank.level_pct});broadcast({type:'PUMP',state:'OFF'});}}
  if(tank.pump==='DRAIN'){tank.level_pct=Math.max(tank.level_pct-0.4,0);tank.volume_L=+(tank.level_pct/100*tank.tank_L).toFixed(1);if(tank.level_pct<=tank.low_pct){tank.pump='OFF';broadcast({type:'AUTOSTOP',reason:'low_level',level_pct:tank.level_pct});broadcast({type:'PUMP',state:'OFF'});}}
  if(tank.pump==='OFF'&&tank.level_pct>0){tank.level_pct=Math.max(+(tank.level_pct-0.02).toFixed(2),0);tank.volume_L=+(tank.level_pct/100*tank.tank_L).toFixed(1);}
  broadcast({type:'UPDATE',level_pct:+tank.level_pct.toFixed(1),volume_L:+tank.volume_L.toFixed(1),tank_L:tank.tank_L,pump:tank.pump,system:tank.system,leak:tank.leak,unit:tank.unit});
},2000);
wss.on('connection',ws=>{
  console.log('Client connected');
  send(ws,{type:'READY',calibrated:tank.calibrated,volume_set:tank.volume_set,volume_L:tank.tank_L,unit:tank.unit,low_pct:tank.low_pct,high_pct:tank.high_pct,inflow_Lps:tank.inflow_Lps,system:tank.system,message:'ready'});
  ws.on('message',raw=>{
    const cmd=raw.toString().trim().toUpperCase();
    console.log('CMD:',cmd);
    if(cmd==='FILL'){tank.pump='FILL';send(ws,{type:'PUMP',state:'FILL'});}
    else if(cmd==='DRAIN'){tank.pump='DRAIN';send(ws,{type:'PUMP',state:'DRAIN'});}
    else if(cmd==='STOP'){tank.pump='OFF';tank.fillTarget=null;send(ws,{type:'PUMP',state:'OFF'});}
    else if(cmd.startsWith('FILLTO ')){const p=parseFloat(cmd.split(' ')[1]);if(!isNaN(p)){tank.fillTarget=p;tank.pump='FILL';send(ws,{type:'PUMP',state:'FILL'});}}
    else if(cmd==='STATUS'){send(ws,{type:'STATUS',level_pct:+tank.level_pct.toFixed(1),volume_L:+tank.volume_L.toFixed(1),tank_L:tank.tank_L,pump:tank.pump,system:tank.system,leak:tank.leak,unit:tank.unit});}
    else if(cmd==='LAST7DAYS'){const sum=tank.dailyUsage.reduce((a,b)=>a+b,0);send(ws,{type:'LAST7DAYS',unit:tank.unit,days:tank.dailyUsage,avg:+(sum/7).toFixed(1),total:+sum.toFixed(1)});}
    else if(cmd==='LASTMONTH'){const sum=tank.monthlyUsage.reduce((a,b)=>a+b,0);send(ws,{type:'LASTMONTH',unit:tank.unit,days:tank.monthlyUsage,avg:+(sum/30).toFixed(1),total:+sum.toFixed(1)});}
    else if(cmd==='PREDICT'){const valid=tank.dailyUsage.filter(d=>d>0);if(!valid.length){send(ws,{type:'PREDICT',error:'not_enough_data'});}else{const avg=valid.reduce((a,b)=>a+b,0)/valid.length;const days=tank.volume_L/avg;send(ws,{type:'PREDICT',current_L:+tank.volume_L.toFixed(1),avg_daily_L:+avg.toFixed(1),days_left:+days.toFixed(1),hours_left:+(days*24).toFixed(0),unit:tank.unit});}}
    else if(cmd==='DIAGNOSTIC'){send(ws,{type:'DIAGNOSTIC',sensor_ok:true,flash_ok:true,calibrated:tank.calibrated,volume_set:tank.volume_set,volume_L:tank.tank_L,inflow_Lps:tank.inflow_Lps,leak_active:tank.leak});}
    else if(cmd.startsWith('SETVOLUME ')){const p=cmd.split(' ');const v=parseFloat(p[1]);const u=p[2]||'L';if(!isNaN(v)&&v>0){tank.tank_L=u==='ML'?v/1000:v;tank.unit=u==='ML'?'mL':'L';tank.volume_L=+(tank.level_pct/100*tank.tank_L).toFixed(1);send(ws,{type:'SETVOLUME_OK',volume_L:tank.tank_L,display:v,unit:tank.unit});}}
    else if(cmd==='SIMULATELEAK'){tank.leak=true;send(ws,{type:'LEAKALERT',rate_pct_per_min:6.3});}
    else if(cmd==='CLEARLEAK'){tank.leak=false;send(ws,{type:'LEAKCLEAR'});}
  });
  ws.on('close',()=>console.log('Client disconnected'));
});
httpServer.listen(PORT,'0.0.0.0',()=>{console.log('\n✓ Water Tank running on port '+PORT+'\n');});
