f = open('index_new.html', 'w')
f.write("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1">
<title>Water Tank</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0;-webkit-tap-highlight-color:transparent}
:root{
--bg:#f0f4f8;--surface:#ffffff;--surface2:#f8fafc;
--border:#e2e8f0;--border2:#cbd5e1;
--text:#0f172a;--text2:#475569;--text3:#94a3b8;
--blue:#2563eb;--blue2:#1d4ed8;--blue-bg:#eff6ff;--blue-bd:#bfdbfe;
--green:#059669;--green-bg:#ecfdf5;--green-bd:#a7f3d0;
--red:#dc2626;--red-bg:#fef2f2;--red-bd:#fecaca;
--amber:#d97706;--amber-bg:#fffbeb;--amber-bd:#fde68a;
--water1:#38bdf8;--water2:#0284c7;
--sh:0 1px 3px rgba(0,0,0,.08),0 4px 16px rgba(0,0,0,.06);
--r:16px;--rs:10px;--r2:22px
}
html,body{height:100%}
body{font-family:"Inter",sans-serif;background:var(--bg);color:var(--text);min-height:100vh;font-size:15px;line-height:1.5}
.screen{display:none;flex-direction:column;min-height:100vh}
.screen.active{display:flex}
#screen-connect{align-items:center;justify-content:center;padding:40px 24px;text-align:center;gap:24px;background:linear-gradient(135deg,#f0f4f8,#dbeafe)}
.c-ring{width:96px;height:96px;border-radius:50%;background:linear-gradient(135deg,var(--blue),var(--water1));display:flex;align-items:center;justify-content:center;font-size:40px;box-shadow:0 8px 32px rgba(37,99,235,.25)}
.c-title{font-size:26px;font-weight:700;letter-spacing:-.5px}
.c-sub{color:var(--text2);font-size:14px;max-width:260px}
.spinner{width:36px;height:36px;border:3px solid var(--border2);border-top-color:var(--blue);border-radius:50%;animation:spin .7s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
#screen-setup{background:var(--bg)}
.setup-inner{padding:56px 24px 36px;display:flex;flex-direction:column;gap:20px;flex:1;min-height:100vh}
.seg-track{display:flex;gap:6px;margin-bottom:4px}
.seg{height:4px;border-radius:2px;flex:1;background:var(--border2);transition:background .4s}
.seg.on{background:var(--blue)}
.s-icon{font-size:32px;margin-bottom:4px}
.s-title{font-size:24px;font-weight:700;letter-spacing:-.4px;line-height:1.2}
.s-body{color:var(--text2);font-size:14px;line-height:1.7}
.info-box{background:var(--amber-bg);border:1.5px solid var(--amber-bd);border-radius:var(--rs);padding:14px 16px;font-size:13px;color:#92400e;line-height:1.6;display:flex;gap:10px}
.prog-track{background:var(--border);border-radius:4px;height:8px;overflow:hidden}
.prog-bar{height:100%;background:linear-gradient(90deg,var(--blue),var(--water1));border-radius:4px;transition:width .5s;width:0%}
.prog-lbl{font-size:13px;color:var(--text3);font-weight:500;text-align:right;margin-top:6px}
.vol-row{display:flex;gap:10px}
.vol-input{flex:1;padding:15px 16px;border:1.5px solid var(--border2);border-radius:var(--rs);font-size:18px;font-weight:600;color:var(--text);background:var(--surface);outline:none;font-family:inherit;transition:border-color .2s}
.vol-input:focus{border-color:var(--blue);box-shadow:0 0 0 3px rgba(37,99,235,.1)}
.unit-btn{padding:15px 18px;border:1.5px solid var(--border2);border-radius:var(--rs);font-size:14px;font-weight:600;color:var(--text2);background:var(--surface);cursor:pointer;white-space:nowrap;transition:all .2s}
.unit-btn:hover{border-color:var(--blue);color:var(--blue)}
.spacer{flex:1}
.btn-p{width:100%;padding:17px;background:linear-gradient(135deg,var(--blue),var(--blue2));color:white;border:none;border-radius:var(--rs);font-size:15px;font-weight:600;cursor:pointer;font-family:inherit;box-shadow:0 4px 12px rgba(37,99,235,.3);transition:all .2s;letter-spacing:-.1px}
.btn-p:active{transform:scale(.98)}
#screen-dashboard{background:var(--bg)}
.d-header{padding:18px 20px 16px;display:flex;align-items:center;justify-content:space-between;background:var(--surface);border-bottom:1px solid var(--border)}
.d-logo{display:flex;align-items:center;gap:10px}
.d-logo-icon{width:34px;height:34px;border-radius:10px;background:linear-gradient(135deg,var(--blue),var(--water1));display:flex;align-items:center;justify-content:center;font-size:16px}
.d-title{font-size:18px;font-weight:700;letter-spacing:-.3px}
.live-pill{display:flex;align-items:center;gap:6px;font-size:12px;font-weight:600;color:var(--green);padding:5px 12px;background:var(--green-bg);border-radius:20px;border:1.5px solid var(--green-bd)}
.live-pill.warn{color:var(--amber);background:var(--amber-bg);border-color:var(--amber-bd)}
.live-pill.err{color:var(--red);background:var(--red-bg);border-color:var(--red-bd)}
.ldot{width:6px;height:6px;border-radius:50%;background:currentColor;animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.4}}
.a-strip{display:none;margin:12px 16px 0;border-radius:var(--rs);padding:11px 16px;font-size:13px;font-weight:500;align-items:center;gap:10px;border:1.5px solid}
.a-strip.on{display:flex}
.a-strip.leak{background:var(--red-bg);border-color:var(--red-bd);color:var(--red)}
.a-strip.afill{background:var(--blue-bg);border-color:var(--blue-bd);color:var(--blue)}
.a-strip.adrain{background:var(--amber-bg);border-color:var(--amber-bd);color:var(--amber)}
.mini-spin{width:14px;height:14px;border:2px solid currentColor;border-top-color:transparent;border-radius:50%;animation:spin .7s linear infinite;flex-shrink:0}
.tab-panels{flex:1;overflow-y:auto}
.tab-panel{display:none;padding:20px}
.tab-panel.active{display:block}
.tank-card{background:var(--surface);border-radius:var(--r2);padding:28px 24px 24px;margin-bottom:16px;box-shadow:var(--sh);display:flex;flex-direction:column;align-items:center;gap:0}
.tank-wrap{position:relative;width:120px;height:160px}
.tank-svg{width:100%;height:100%}
.tank-labels{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;pointer-events:none;gap:3px}
.t-pct{font-size:28px;font-weight:700;color:var(--text);letter-spacing:-1px;line-height:1}
.t-vol{font-size:12px;color:var(--text2);font-weight:500}
.pred-pill{margin-top:16px;display:inline-flex;align-items:center;gap:6px;font-size:13px;font-weight:600;padding:7px 16px;border-radius:20px;border:1.5px solid}
.pred-pill.good{color:var(--green);background:var(--green-bg);border-color:var(--green-bd)}
.pred-pill.warn{color:var(--amber);background:var(--amber-bg);border-color:var(--amber-bd)}
.pred-pill.crit{color:var(--red);background:var(--red-bg);border-color:var(--red-bd)}
.pred-pill.neu{color:var(--text2);background:var(--surface2);border-color:var(--border)}
.ctrl-row{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:14px}
.ctrl{padding:20px 16px;border-radius:var(--r);border:1.5px solid;cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:8px;font-family:inherit;transition:all .15s;box-shadow:var(--sh);background:var(--surface)}
.ctrl:active{transform:scale(.97)}
.ctrl:disabled{opacity:.4;pointer-events:none}
.c-icon{font-size:26px}
.c-lbl{font-size:13px;font-weight:600}
.c-sub{font-size:11px;opacity:.7}
.ctrl.fill{background:var(--blue-bg);border-color:var(--blue-bd);color:var(--blue)}
.ctrl.drain{background:var(--amber-bg);border-color:var(--amber-bd);color:var(--amber)}
.stop-btn{width:100%;padding:15px;border-radius:var(--r);background:var(--red-bg);border:1.5px solid var(--red-bd);color:var(--red);font-size:14px;font-weight:600;cursor:pointer;font-family:inherit;margin-bottom:14px;display:none;align-items:center;justify-content:center;gap:8px;box-shadow:var(--sh);transition:all .15s}
.stop-btn.show{display:flex}
.stop-btn:active{transform:scale(.98)}
.fcard{background:var(--surface);border-radius:var(--r);padding:18px 20px;box-shadow:var(--sh)}
.fcard-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.fcard-title{font-size:14px;font-weight:600}
.fcard-val{font-size:22px;font-weight:700;color:var(--blue);letter-spacing:-.5px}
input[type=range]{width:100%;height:6px;-webkit-appearance:none;appearance:none;background:var(--border2);border-radius:3px;outline:none;cursor:pointer;margin-bottom:14px}
input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;width:22px;height:22px;border-radius:50%;background:var(--blue);box-shadow:0 2px 8px rgba(37,99,235,.4)}
.f-btn{width:100%;padding:13px;border-radius:var(--rs);background:var(--blue);color:white;border:none;font-size:14px;font-weight:600;cursor:pointer;font-family:inherit;box-shadow:0 4px 12px rgba(37,99,235,.25);transition:all .15s}
.f-btn:active{transform:scale(.98)}
.sec-title{font-size:18px;font-weight:700;letter-spacing:-.3px;margin-bottom:4px}
.sec-sub{font-size:13px;color:var(--text2);margin-bottom:20px}
.chart-card{background:var(--surface);border-radius:var(--r);padding:20px;box-shadow:var(--sh);margin-bottom:20px}
.chart-lbl{font-size:13px;font-weight:600;color:var(--text2);margin-bottom:14px}
.bars{display:flex;align-items:flex-end;gap:5px;height:160px}
.bc{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:4px;height:100%}
.bb{width:100%;border-radius:6px 6px 0 0;min-height:4px;transition:height .6s cubic-bezier(.34,1.56,.64,1)}
.bnum{font-size:10px;font-weight:600;color:var(--text2)}
.blbl{font-size:10px;color:var(--text3);font-weight:500}
.stats-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:16px}
.stat{background:var(--surface2);border-radius:var(--rs);padding:14px;border:1px solid var(--border)}
.stat-l{font-size:11px;color:var(--text3);font-weight:600;text-transform:uppercase;letter-spacing:.05em;margin-bottom:4px}
.stat-n{font-size:20px;font-weight:700;color:var(--text);letter-spacing:-.5px}
.stat-u{font-size:12px;color:var(--text2);font-weight:500}
.al-item{display:flex;align-items:center;gap:16px;padding:18px 0;border-bottom:1px solid var(--border)}
.al-item:last-child{border-bottom:none}
.al-ico{width:40px;height:40px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0}
.al-text{flex:1}
.al-name{font-size:14px;font-weight:600}
.al-desc{font-size:12px;color:var(--text2);margin-top:2px}
.tog{width:48px;height:28px;background:var(--border2);border-radius:14px;position:relative;cursor:pointer;border:none;transition:background .25s;flex-shrink:0}
.tog.on{background:var(--blue)}
.tog::after{content:"";position:absolute;width:22px;height:22px;background:white;border-radius:50%;top:3px;left:3px;transition:transform .25s;box-shadow:0 1px 4px rgba(0,0,0,.25)}
.tog.on::after{transform:translateX(20px)}
.sg{margin-bottom:24px}
.sg-title{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--text3);margin-bottom:8px}
.sc{background:var(--surface);border-radius:var(--r);overflow:hidden;box-shadow:var(--sh)}
.sr{display:flex;align-items:center;justify-content:space-between;padding:15px 18px;border-bottom:1px solid var(--border);font-size:14px}
.sr:last-child{border-bottom:none}
.sr.tap{cursor:pointer;transition:background .15s}
.sr.tap:active{background:var(--surface2)}
.sl{font-size:13px;color:var(--text2)}
.sv{font-size:14px;font-weight:600}
.sa{font-size:13px;color:var(--blue);font-weight:600;background:none;border:none;cursor:pointer;font-family:inherit}
.dr{display:flex;align-items:center;gap:12px;padding:13px 0;border-bottom:1px solid var(--border)}
.dr:last-child{border-bottom:none}
.dd{width:10px;height:10px;border-radius:50%;flex-shrink:0}
.dd.ok{background:var(--green)}.dd.warn{background:var(--amber)}
.tab-bar{display:flex;background:var(--surface);border-top:1px solid var(--border);position:sticky;bottom:0;z-index:10}
.tab{flex:1;padding:10px 4px 12px;display:flex;flex-direction:column;align-items:center;gap:3px;cursor:pointer;font-size:11px;font-weight:600;color:var(--text3);border:none;background:none;font-family:inherit;transition:color .2s}
.ti{font-size:22px;line-height:1}
.tab.active{color:var(--blue)}
.toast{position:fixed;bottom:84px;left:50%;transform:translateX(-50%);padding:11px 22px;border-radius:24px;font-size:13px;font-weight:600;color:white;z-index:999;white-space:nowrap;box-shadow:0 4px 20px rgba(0,0,0,.2);animation:tin .3s cubic-bezier(.34,1.56,.64,1)}
@keyframes tin{from{opacity:0;transform:translateX(-50%) translateY(12px)}}
@media(min-width:600px){
  body{background:#dde3ea;display:flex;justify-content:center}
  #screen-connect,#screen-setup{max-width:420px;width:100%}
  #screen-dashboard{max-width:420px;width:100%;box-shadow:0 0 80px rgba(0,0,0,.15);min-height:100vh}
}
</style>
</head>
<body>

<div id="screen-connect" class="screen active">
  <div class="c-ring">&#128167;</div>
  <div class="c-title">Water Tank</div>
  <div class="c-sub">Connecting to your device&hellip;</div>
  <div class="spinner"></div>
  <div id="cmsg" style="font-size:13px;color:var(--text3);font-weight:500">Starting up</div>
</div>

<div id="screen-setup" class="screen">
  <div class="setup-inner">
    <div id="ss1">
      <div class="seg-track"><div class="seg on"></div><div class="seg"></div></div>
      <div class="s-icon">&#128268;</div>
      <div class="s-title">Set up your sensor</div>
      <div class="s-body" style="margin-top:10px">Make sure your tank is <strong>completely empty</strong> and the ultrasonic sensor points straight down from the top.</div>
      <div class="info-box" style="margin-top:16px"><span style="font-size:16px;flex-shrink:0">&#128161;</span><span>The sensor measures the empty tank height first. Keep everything still &mdash; takes about 30 seconds.</span></div>
      <div class="spacer"></div>
      <button class="btn-p" onclick="startCal()">My tank is empty &mdash; start</button>
    </div>
    <div id="scal" style="display:none">
      <div class="seg-track"><div class="seg on"></div><div class="seg"></div></div>
      <div class="s-icon">&#128300;</div>
      <div class="s-title">Measuring&hellip;</div>
      <div class="s-body" style="margin-top:10px">Keep the tank still and empty.</div>
      <div style="margin-top:24px"><div class="prog-track"><div class="prog-bar" id="cal-bar"></div></div><div class="prog-lbl" id="cal-lbl">Sample 0 / 30</div></div>
      <div id="cal-msg" class="s-body" style="margin-top:16px"></div>
    </div>
    <div id="svol" style="display:none">
      <div class="seg-track"><div class="seg on"></div><div class="seg on"></div></div>
      <div class="s-icon">&#128200;</div>
      <div class="s-title">How big is your tank?</div>
      <div class="s-body" style="margin-top:10px">Check the label on your tank. Common sizes: 500 L, 1000 L, 2000 L</div>
      <div class="vol-row" style="margin-top:20px">
        <input class="vol-input" type="number" id="vol-input" placeholder="e.g. 500" min="1"/>
        <button class="unit-btn" id="unit-btn" onclick="toggleUnit()">Litres</button>
      </div>
      <div class="spacer"></div>
      <button class="btn-p" onclick="saveVol()">Save and open my tank</button>
    </div>
  </div>
</div>

<div id="screen-dashboard" class="screen">
  <div class="d-header">
    <div class="d-logo">
      <div class="d-logo-icon">&#128167;</div>
      <div class="d-title">My Tank</div>
    </div>
    <div class="live-pill" id="live-pill"><div class="ldot"></div><span id="live-txt">Live</span></div>
  </div>
  <div class="a-strip leak" id="as-leak"><span style="font-size:15px">&#9888;</span>Level dropping fast &mdash; possible leak</div>
  <div class="a-strip afill" id="as-fill"><div class="mini-spin"></div><span id="fill-txt">Filling&hellip; stops when full</span></div>
  <div class="a-strip adrain" id="as-drain"><div class="mini-spin"></div><span>Draining&hellip; stops at minimum</span></div>

  <div class="tab-panels">

    <div id="panel-home" class="tab-panel active">
      <div class="tank-card">
        <div class="tank-wrap">
          <svg class="tank-svg" viewBox="0 0 120 160" fill="none">
            <defs>
              <clipPath id="tc"><rect x="8" y="8" width="104" height="144" rx="12"/></clipPath>
              <linearGradient id="wg" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0%" stop-color="#38bdf8"/>
                <stop offset="100%" stop-color="#0284c7"/>
              </linearGradient>
            </defs>
            <rect x="8" y="8" width="104" height="144" rx="12" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2"/>
            <rect id="wrect" x="8" y="152" width="104" height="0" fill="url(#wg)" clip-path="url(#tc)" style="transition:y 1.4s ease,height 1.4s ease"/>
            <rect x="8" y="8" width="104" height="144" rx="12" fill="none" stroke="#cbd5e1" stroke-width="1.5"/>
            <line x1="10" y1="56" x2="18" y2="56" stroke="#e2e8f0" stroke-width="1.5"/>
            <line x1="10" y1="104" x2="18" y2="104" stroke="#e2e8f0" stroke-width="1.5"/>
          </svg>
          <div class="tank-labels">
            <div class="t-pct" id="t-pct">58%</div>
            <div class="t-vol" id="t-vol">290 L</div>
          </div>
        </div>
        <div class="pred-pill neu" id="pred-pill">Calculating&hellip;</div>
      </div>

      <div class="ctrl-row">
        <button class="ctrl fill" id="btn-fill" onclick="sendCmd('FILL')">
          <span class="c-icon">&#9650;</span>
          <span class="c-lbl">Fill tank</span>
          <span class="c-sub">Auto-stops when full</span>
        </button>
        <button class="ctrl drain" id="btn-drain" onclick="sendCmd('DRAIN')">
          <span class="c-icon">&#9660;</span>
          <span class="c-lbl">Drain</span>
          <span class="c-sub">Auto-stops at min</span>
        </button>
      </div>

      <button class="stop-btn" id="btn-stop" onclick="sendCmd('STOP')">
        <span style="font-size:18px">&#9632;</span> Stop pump
      </button>

      <div class="fcard">
        <div class="fcard-top">
          <div class="fcard-title">Fill to target</div>
          <div class="fcard-val" id="fval">80%</div>
        </div>
        <input type="range" min="10" max="95" value="80" id="fslider" oninput="document.getElementById('fval').textContent=this.value+'%'">
        <button class="f-btn" onclick="doFillTo()">Fill to this level</button>
      </div>
    </div>

    <div id="panel-usage" class="tab-panel">
      <div class="sec-title">Usage</div>
      <div class="sec-sub" id="usage-sub">Loading usage data&hellip;</div>
      <div class="chart-card">
        <div class="chart-lbl">This week</div>
        <div class="bars" id="week-chart"><div style="flex:1;display:flex;align-items:center;justify-content:center;color:var(--text3);font-size:13px">Loading&hellip;</div></div>
        <div class="stats-grid" id="week-stats" style="display:none">
          <div class="stat"><div class="stat-l">Daily average</div><div><span class="stat-n" id="s-avg">-</span> <span class="stat-u" id="s-unit">L</span></div></div>
          <div class="stat"><div class="stat-l">Week total</div><div><span class="stat-n" id="s-tot">-</span> <span class="stat-u" id="s-unit2">L</span></div></div>
        </div>
      </div>
      <div class="chart-card">
        <div class="chart-lbl">Last 30 days</div>
        <div class="bars" id="month-chart"><div style="flex:1;display:flex;align-items:center;justify-content:center;color:var(--text3);font-size:13px">Loading&hellip;</div></div>
      </div>
    </div>

    <div id="panel-alerts" class="tab-panel">
      <div class="sec-title">Alerts</div>
      <div class="sec-sub">Choose when to get notified</div>
      <div style="background:var(--surface);border-radius:var(--r);padding:4px 20px;box-shadow:var(--sh)">
        <div class="al-item"><div class="al-ico" style="background:#fef9c3">&#128293;</div><div class="al-text"><div class="al-name">Getting low</div><div class="al-desc">When tank drops below 25%</div></div><button class="tog on" onclick="this.classList.toggle('on')"></button></div>
        <div class="al-item"><div class="al-ico" style="background:#fee2e2">&#9888;</div><div class="al-text"><div class="al-name">Almost empty</div><div class="al-desc">When tank drops below 10%</div></div><button class="tog on" onclick="this.classList.toggle('on')"></button></div>
        <div class="al-item"><div class="al-ico" style="background:#dcfce7">&#9989;</div><div class="al-text"><div class="al-name">Tank is full</div><div class="al-desc">When filling completes</div></div><button class="tog" onclick="this.classList.toggle('on')"></button></div>
        <div class="al-item"><div class="al-ico" style="background:#ede9fe">&#128167;</div><div class="al-text"><div class="al-name">Possible leak</div><div class="al-desc">Level drops fast while pump is off</div></div><button class="tog on" onclick="this.classList.toggle('on')"></button></div>
      </div>
    </div>

    <div id="panel-settings" class="tab-panel">
      <div class="sec-title">Settings</div>
      <div class="sec-sub">Device configuration</div>
      <div class="sg">
        <div class="sg-title">Tank</div>
        <div class="sc">
          <div class="sr"><span class="sl">Capacity</span><span class="sv" id="set-cap">500 L</span></div>
          <div class="sr"><span class="sl">Low threshold</span><span class="sv" id="set-low">5%</span></div>
          <div class="sr"><span class="sl">High threshold</span><span class="sv" id="set-high">95%</span></div>
          <div class="sr"><span class="sl">Flow rate</span><span class="sv" id="set-flow">-</span></div>
        </div>
      </div>
      <div class="sg">
        <div class="sg-title">Diagnostics</div>
        <div class="sc">
          <div class="sr"><span class="sl">System check</span><button class="sa" onclick="sendCmd('DIAGNOSTIC')">Run &#8594;</button></div>
          <div id="diag-out" style="padding:0 18px"></div>
        </div>
      </div>
      <div class="sg">
        <div class="sg-title">Sensor</div>
        <div class="sc">
          <div class="sr tap" onclick="recal()"><div><div style="font-size:14px;font-weight:500">Re-run calibration</div><div class="sl" style="margin-top:2px">Empty the tank first</div></div><span style="color:var(--text3);font-size:18px">&#8250;</span></div>
        </div>
      </div>
    </div>

  </div>

  <div class="tab-bar">
    <button class="tab active" onclick="st('home',this)"><span class="ti">&#127968;</span>Home</button>
    <button class="tab" onclick="st('usage',this)"><span class="ti">&#128202;</span>Usage</button>
    <button class="tab" onclick="st('alerts',this)"><span class="ti">&#128276;</span>Alerts</button>
    <button class="tab" onclick="st('settings',this)"><span class="ti">&#9881;</span>Settings</button>
  </div>
</div>

<script>
var S={tank_L:500,unit:"L",pump:"OFF",low:5,high:95,inflow:-1};
var ws,rt;
function conn(){
  ws=new WebSocket("ws://"+location.host);
  ws.onopen=function(){clearTimeout(rt);setMsg("Connected \u2014 waiting for device...");};
  ws.onmessage=function(e){var m;try{m=JSON.parse(e.data)}catch(x){return}hnd(m);};
  ws.onclose=function(){show("connect");setMsg("Reconnecting...");rt=setTimeout(conn,2000);};
  ws.onerror=function(){ws.close();};
}
function sendCmd(c){if(ws&&ws.readyState===1)ws.send(c);}
function hnd(m){
  if(m.type==="READY"){
    S.tank_L=m.volume_L||500;S.unit=m.unit||"L";S.low=m.low_pct||5;S.high=m.high_pct||95;S.inflow=m.inflow_Lps||-1;
    updSet();
    if(!m.calibrated){show("setup");stp("s1");}
    else if(!m.volume_set){show("setup");stp("vol");}
    else{show("dashboard");sendCmd("STATUS");sendCmd("PREDICT");sendCmd("LAST7DAYS");sendCmd("LASTMONTH");}
  }
  else if(m.type==="UPDATE"||m.type==="STATUS"){
    S.pump=m.pump;S.tank_L=m.tank_L||S.tank_L;S.unit=m.unit||S.unit;
    updTank(m.level_pct,m.volume_L);updBadge(m.system,m.leak);
    if(m.leak)document.getElementById("as-leak").classList.add("on");
    updPump(m.pump);
  }
  else if(m.type==="PUMP"){updPump(m.state);}
  else if(m.type==="AUTOSTOP"){toast(m.reason==="high_level"?"Tank full \u2014 pump stopped":"Reached minimum \u2014 pump stopped","green");updPump("OFF");}
  else if(m.type==="SAFETYSTOP"){toast("Pump stopped \u2014 level not changing. Check the pump.","amber");}
  else if(m.type==="FILLTO_DONE"){toast("Filled to "+Math.round(m.actual_pct)+"%","green");updPump("OFF");}
  else if(m.type==="LEAKALERT"){document.getElementById("as-leak").classList.add("on");}
  else if(m.type==="LEAKCLEAR"){document.getElementById("as-leak").classList.remove("on");}
  else if(m.type==="CAL_PROGRESS"){
    document.getElementById("cal-bar").style.width=Math.round(m.sample/m.total*100)+"%";
    document.getElementById("cal-lbl").textContent="Sample "+m.sample+" / "+m.total;
  }
  else if(m.type==="CAL_VERIFY"){document.getElementById("cal-bar").style.width="100%";document.getElementById("cal-lbl").textContent="Verifying...";document.getElementById("cal-msg").textContent="Pour a little water in to verify...";}
  else if(m.type==="CAL_OK"){stp("vol");}
  else if(m.type==="CAL_FAIL"){document.getElementById("cal-msg").textContent="Issue detected. Retrying...";}
  else if(m.type==="SETVOLUME_OK"){S.tank_L=m.volume_L;S.unit=m.unit;updSet();show("dashboard");sendCmd("STATUS");sendCmd("PREDICT");sendCmd("LAST7DAYS");sendCmd("LASTMONTH");}
  else if(m.type==="LAST7DAYS"){rWeek(m);}
  else if(m.type==="LASTMONTH"){rMonth(m);}
  else if(m.type==="PREDICT"){
    var p=document.getElementById("pred-pill");
    if(m.error){p.className="pred-pill neu";p.textContent="Not enough data yet";return;}
    var d=Math.floor(m.days_left);
    if(d<=1){p.className="pred-pill crit";p.innerHTML="&#9888; Less than a day remaining";}
    else if(d<=3){p.className="pred-pill warn";p.innerHTML="&#9203; ~"+d+" days remaining";}
    else{p.className="pred-pill good";p.innerHTML="&#10003; ~"+d+" days remaining";}
  }
  else if(m.type==="DIAGNOSTIC"){
    var rows=[["Ultrasonic sensor",m.sensor_ok],["Flash storage",m.flash_ok],["Calibrated",m.calibrated],["Volume set",m.volume_set]];
    document.getElementById("diag-out").innerHTML=rows.map(function(r){
      return "<div class='dr'><div class='dd "+(r[1]?"ok":"warn")+"'></div><div style='flex:1;font-size:14px;font-weight:500'>"+r[0]+"</div><span style='font-size:13px;font-weight:600;color:"+(r[1]?"var(--green)":"var(--amber)")+"'>"+(r[1]?"OK":"Check")+"</span></div>";
    }).join("");
  }
}
function updTank(pct,vol){
  document.getElementById("t-pct").textContent=Math.round(pct)+"%";
  document.getElementById("t-vol").textContent=Math.round(vol)+" "+S.unit;
  var h=pct/100*144;
  var r=document.getElementById("wrect");
  r.setAttribute("y",String(152-h));
  r.setAttribute("height",String(h));
}
function updBadge(sys,leak){
  var b=document.getElementById("live-pill"),t=document.getElementById("live-txt");
  b.className="live-pill";
  if(sys==="ERROR"){b.classList.add("err");t.textContent="Sensor error";}
  else if(sys==="WARN"||leak){b.classList.add("warn");t.textContent="Warning";}
  else{t.textContent="Live";}
}
function updPump(p){
  S.pump=p;
  var sf=document.getElementById("as-fill"),sd=document.getElementById("as-drain");
  var sb=document.getElementById("btn-stop");
  var bf=document.getElementById("btn-fill"),bd=document.getElementById("btn-drain");
  sf.classList.remove("on");sd.classList.remove("on");sb.classList.remove("show");
  bf.disabled=false;bd.disabled=false;
  if(p==="FILL"){sf.classList.add("on");sb.classList.add("show");bf.disabled=true;bd.disabled=true;}
  else if(p==="DRAIN"){sd.classList.add("on");sb.classList.add("show");bf.disabled=true;bd.disabled=true;}
}
function rWeek(m){
  var max=Math.max.apply(null,m.days.concat([1]));
  var days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"];
  document.getElementById("week-chart").innerHTML=m.days.map(function(v,i){
    var h=Math.max(v/max*100,3);
    var c=i===6?"#0284c7":"#93c5fd";
    return "<div class='bc'><div class='bnum'>"+Math.round(v)+"</div><div class='bb' style='height:"+h+"%;background:"+c+"'></div><div class='blbl'>"+days[i]+"</div></div>";
  }).join("");
  document.getElementById("week-stats").style.display="grid";
  document.getElementById("s-avg").textContent=m.avg;
  document.getElementById("s-tot").textContent=m.total;
  document.getElementById("s-unit").textContent=m.unit;
  document.getElementById("s-unit2").textContent=m.unit;
  document.getElementById("usage-sub").textContent="Your average is "+m.avg+" "+m.unit+" per day";
}
function rMonth(m){
  var max=Math.max.apply(null,m.days.concat([1]));
  document.getElementById("month-chart").innerHTML=m.days.map(function(v){
    var h=Math.max(v/max*100,3);
    return "<div class='bc'><div class='bb' style='height:"+h+"%;background:#bae6fd'></div></div>";
  }).join("");
}
var uUnit="L";
function toggleUnit(){uUnit=uUnit==="L"?"mL":"L";document.getElementById("unit-btn").textContent=uUnit==="L"?"Litres":"Millilitres";}
function saveVol(){
  var v=parseFloat(document.getElementById("vol-input").value);
  if(!v||v<=0){alert("Please enter a valid tank size");return;}
  sendCmd("SETVOLUME "+v+" "+uUnit);
}
function startCal(){stp("cal");sendCmd("CALIBRATE");}
function doFillTo(){sendCmd("FILLTO "+document.getElementById("fslider").value);}
function recal(){if(confirm("Empty the tank first. Continue?")){show("setup");stp("s1");}}
function updSet(){
  document.getElementById("set-cap").textContent=Math.round(S.tank_L)+" "+(S.unit||"L");
  document.getElementById("set-low").textContent=(S.low||5)+"%";
  document.getElementById("set-high").textContent=(S.high||95)+"%";
  document.getElementById("set-flow").textContent=S.inflow>0?(S.inflow*60).toFixed(1)+" L/min":"Not calibrated";
}
function show(n){document.querySelectorAll(".screen").forEach(function(s){s.classList.remove("active");});document.getElementById("screen-"+n).classList.add("active");}
function stp(s){["s1","cal","vol"].forEach(function(x){var e=document.getElementById("s"+x);if(e)e.style.display=x===s?"":"none";});}
function st(n,btn){
  document.querySelectorAll(".tab-panel").forEach(function(p){p.classList.remove("active");});
  document.querySelectorAll(".tab").forEach(function(t){t.classList.remove("active");});
  document.getElementById("panel-"+n).classList.add("active");btn.classList.add("active");
  if(n==="usage"){sendCmd("LAST7DAYS");sendCmd("LASTMONTH");}
}
function setMsg(t){var e=document.getElementById("cmsg");if(e)e.innerHTML=t;}
function toast(msg,color){
  var t=document.createElement("div");t.className="toast";t.innerHTML=msg;
  t.style.background=color==="green"?"var(--green)":color==="amber"?"var(--amber)":"#1e293b";
  document.body.appendChild(t);setTimeout(function(){t.remove();},3500);
}
conn();
</script>
</body>
</html>""")
f.close()
import os
import shutil
shutil.move('index_new.html','index.html')
print("Done! " + str(os.path.getsize('index.html')) + " bytes")
