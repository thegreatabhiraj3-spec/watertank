import re, os

path = '/home/abhiraj/watertank/index.html'
content = open(path).read()

GEMINI_KEY = 'AIzaSyDz8x5hGY8KQVQ8i3qnvOPPiVT_8PvNTbk'

# ── 1. Add Aqua button to opening screen ───────────────────
old_cards = '''  <div class="card" onclick="selectMode('bluetooth')">'''

# Find the full opening screen cards section
opening_match = re.search(r'(<div id="screen-opening".*?</div>\s*</div>\s*</div>)', content, re.DOTALL)

old_opening = '''  <div class="card" onclick="selectMode('bluetooth')">'''

# Add Ask Aqua card after WiFi card
old_wifi_card_end = '''  <div class="card" onclick="selectMode('wifi')">'''

# Find both cards and add Aqua card after wifi
aqua_card = '''
  <!-- Ask Aqua button -->
  <div class="card aqua-card" onclick="openAquaChat()" style="background:linear-gradient(135deg,#1e1b4b,#312e81);border:none;margin-top:8px;">
    <div style="display:flex;align-items:center;gap:14px;">
      <div style="width:48px;height:48px;border-radius:14px;background:rgba(255,255,255,0.15);display:flex;align-items:center;justify-content:center;font-size:24px;flex-shrink:0;">🤖</div>
      <div>
        <div style="font-size:16px;font-weight:700;color:white;">Ask Aqua</div>
        <div style="font-size:13px;color:rgba(255,255,255,0.6);margin-top:2px;">Water advisor & tank assistant</div>
      </div>
      <div style="margin-left:auto;color:rgba(255,255,255,0.4);font-size:20px;">›</div>
    </div>
  </div>'''

# Find where the opening screen cards end and insert aqua card
# Look for the closing of the opening screen div
old_end_opening = '</div>\n\n<!-- ===================='
new_end_opening = aqua_card + '\n</div>\n\n<!-- ===================='

if old_end_opening in content:
    content = content.replace(old_end_opening, new_end_opening, 1)
    print('✓ Aqua card added to opening screen')
else:
    # Try alternate
    old_end_opening2 = '</div>\n<!-- ===================='
    if old_end_opening2 in content:
        content = content.replace(old_end_opening2, aqua_card + '\n</div>\n<!-- ====================', 1)
        print('✓ Aqua card added (alt method)')
    else:
        print('WARNING: Could not find opening screen end')

# ── 2. Add Aqua chat screen ─────────────────────────────────
aqua_screen = '''
<!-- ==================== AQUA CHAT SCREEN ==================== -->
<div id="screen-aqua" class="screen">
  <div style="background:linear-gradient(135deg,#1e1b4b,#312e81);padding:20px 20px 16px;display:flex;align-items:center;gap:12px;">
    <button onclick="goBack()" style="background:rgba(255,255,255,0.15);border:none;color:white;width:36px;height:36px;border-radius:50%;font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;">←</button>
    <div style="flex:1;">
      <div style="font-size:17px;font-weight:700;color:white;display:flex;align-items:center;gap:8px;">
        <div id="aqua-status-dot" style="width:8px;height:8px;border-radius:50%;background:#4ade80;animation:pulse-green 2s infinite;"></div>
        Aqua
      </div>
      <div style="font-size:12px;color:rgba(255,255,255,0.5);margin-top:1px;">AquaIQ water assistant</div>
    </div>
    <div id="aqua-tank-badge" style="display:none;background:rgba(255,255,255,0.15);padding:5px 11px;border-radius:20px;font-size:12px;font-weight:600;color:white;">
      Tank: <span id="aqua-level-badge">--</span>
    </div>
  </div>

  <div id="aqua-messages" style="flex:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:10px;background:#f5f7fa;"></div>

  <!-- Suggestion pills -->
  <div id="aqua-pills" style="display:flex;flex-wrap:wrap;gap:6px;padding:10px 14px;background:#f5f7fa;border-top:1px solid #e2e8f0;">
    <button class="aqua-pill" onclick="usePill(this)">How\'s my tank?</button>
    <button class="aqua-pill" onclick="usePill(this)">How long will water last?</button>
    <button class="aqua-pill" onclick="usePill(this)">Water saving tips</button>
    <button class="aqua-pill" onclick="usePill(this)">Should I fill now?</button>
  </div>

  <!-- Confirm action buttons (hidden until needed) -->
  <div id="aqua-confirm" style="display:none;padding:10px 14px;background:white;border-top:1px solid #e2e8f0;">
    <div id="aqua-confirm-text" style="font-size:13px;color:#475569;margin-bottom:8px;text-align:center;"></div>
    <div style="display:flex;gap:8px;">
      <button id="aqua-confirm-yes" onclick="confirmAction(true)" style="flex:1;padding:11px;background:#2563eb;color:white;border:none;border-radius:10px;font-size:14px;font-weight:600;cursor:pointer;font-family:inherit;">Yes, do it</button>
      <button onclick="confirmAction(false)" style="flex:1;padding:11px;background:#f1f5f9;color:#475569;border:none;border-radius:10px;font-size:14px;font-weight:500;cursor:pointer;font-family:inherit;">No thanks</button>
    </div>
  </div>

  <div style="display:flex;gap:8px;padding:10px 12px 14px;background:white;border-top:1px solid #e2e8f0;align-items:flex-end;">
    <input id="aqua-input" type="text" placeholder="Ask about your water..."
      style="flex:1;padding:11px 16px;border:1.5px solid #cbd5e1;border-radius:22px;font-size:14px;color:#0a1929;background:#f8fafc;outline:none;font-family:inherit;"
      onkeydown="if(event.key==='Enter')sendAqua()"
      onfocus="this.style.borderColor='#2563eb'"
      onblur="this.style.borderColor='#cbd5e1'"/>
    <button onclick="sendAqua()" style="width:42px;height:42px;border-radius:50%;background:linear-gradient(135deg,#2563eb,#1d4ed8);color:white;border:none;cursor:pointer;font-size:17px;display:flex;align-items:center;justify-content:center;flex-shrink:0;box-shadow:0 2px 8px rgba(37,99,235,0.35);">↑</button>
  </div>
</div>

'''

# Insert Aqua screen before the dashboard screen
content = content.replace('<div id="screen-dashboard"', aqua_screen + '<div id="screen-dashboard"')
print('✓ Aqua chat screen added')

# ── 3. Add CSS for Aqua ─────────────────────────────────────
aqua_css = '''
    @keyframes pulse-green { 0%,100%{opacity:1} 50%{opacity:0.4} }
    .aqua-card { cursor: pointer; transition: transform 0.15s; }
    .aqua-card:active { transform: scale(0.98); }
    .aqua-msg-bot {
      max-width: 82%; padding: 11px 15px;
      background: white; border: 1px solid #e2e8f0;
      border-radius: 18px 18px 18px 4px;
      font-size: 14px; line-height: 1.55;
      color: #0a1929; align-self: flex-start;
      box-shadow: 0 1px 4px rgba(0,0,0,0.06);
      word-wrap: break-word;
    }
    .aqua-msg-user {
      max-width: 82%; padding: 11px 15px;
      background: linear-gradient(135deg,#2563eb,#1d4ed8);
      border-radius: 18px 18px 4px 18px;
      font-size: 14px; line-height: 1.55;
      color: white; align-self: flex-end;
      word-wrap: break-word;
    }
    .aqua-typing {
      display: flex; gap: 4px; align-items: center;
      padding: 12px 16px; background: white;
      border: 1px solid #e2e8f0;
      border-radius: 18px 18px 18px 4px;
      align-self: flex-start;
      box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    }
    .aqua-typing span {
      width: 7px; height: 7px; border-radius: 50%;
      background: #94a3b8; animation: bounce 1.2s infinite;
    }
    .aqua-typing span:nth-child(2) { animation-delay: 0.2s; }
    .aqua-typing span:nth-child(3) { animation-delay: 0.4s; }
    @keyframes bounce { 0%,60%,100%{transform:translateY(0)} 30%{transform:translateY(-5px)} }
    .aqua-pill {
      padding: 6px 13px; background: white;
      color: #2563eb; border: 1.5px solid #bfdbfe;
      border-radius: 16px; font-size: 12px;
      font-weight: 500; cursor: pointer;
      font-family: inherit; transition: all 0.15s;
    }
    .aqua-pill:active { background: #eff6ff; transform: scale(0.97); }
    #screen-aqua { display: none; flex-direction: column; height: 100vh; }
    #screen-aqua.active { display: flex; }
'''

content = content.replace('</style>', aqua_css + '\n  </style>')
print('✓ Aqua CSS added')

# ── 4. Add full Aqua JavaScript ─────────────────────────────
aqua_js = f'''
// ==================== AQUA AI CHATBOT ====================
const GEMINI_KEY = '{GEMINI_KEY}';
const GEMINI_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=' + GEMINI_KEY;

var aquaHistory = [];
var aquaPendingAction = null;
var aquaTankData = {{
  connected: false,
  level_pct: null,
  volume_L: null,
  tank_L: 500,
  pump: 'OFF',
  unit: 'L',
  avg_daily: null,
  days_left: null,
  leak: false
}};

function updateAquaData(data) {{
  aquaTankData.connected = true;
  if (data.level_pct !== undefined) aquaTankData.level_pct = data.level_pct;
  if (data.volume_L !== undefined) aquaTankData.volume_L = data.volume_L;
  if (data.tank_L !== undefined) aquaTankData.tank_L = data.tank_L;
  if (data.pump !== undefined) aquaTankData.pump = data.pump;
  if (data.unit !== undefined) aquaTankData.unit = data.unit;
  if (data.leak !== undefined) aquaTankData.leak = data.leak;
  if (data.avg_daily_L !== undefined) aquaTankData.avg_daily = data.avg_daily_L;
  if (data.days_left !== undefined) aquaTankData.days_left = data.days_left;

  // Update badge in chat header
  var badge = document.getElementById('aqua-tank-badge');
  var levelBadge = document.getElementById('aqua-level-badge');
  if (badge && levelBadge && aquaTankData.level_pct !== null) {{
    badge.style.display = 'block';
    levelBadge.textContent = Math.round(aquaTankData.level_pct) + '%';
  }}
}}

function getAquaSystemPrompt() {{
  var tankInfo = '';
  if (aquaTankData.connected && aquaTankData.level_pct !== null) {{
    tankInfo = `
LIVE TANK DATA (user is connected):
- Level: ${{Math.round(aquaTankData.level_pct)}}% full
- Volume: ${{Math.round(aquaTankData.volume_L)}} ${{aquaTankData.unit}} of ${{aquaTankData.tank_L}} ${{aquaTankData.unit}} total capacity
- Pump status: ${{aquaTankData.pump}}
- Average daily usage: ${{aquaTankData.avg_daily || 'unknown'}} ${{aquaTankData.unit}}/day
- Estimated days remaining: ${{aquaTankData.days_left ? '~' + Math.round(aquaTankData.days_left * 10)/10 + ' days' : 'calculating...'}}
- Leak detected: ${{aquaTankData.leak ? 'YES - URGENT' : 'No'}}`;
  }} else {{
    tankInfo = 'TANK STATUS: Not connected to a tank device yet.';
  }}

  return `You are Aqua, the AI water assistant for AquaIQ — a smart home water tank monitoring system. You have a warm, helpful, slightly witty personality. You are like a knowledgeable friend who happens to be an expert on water.

${{tankInfo}}

YOUR PERSONALITY:
- Warm, concise, conversational — like texting a smart friend
- Never robotic or overly formal
- Use the user's context smartly (if they say "going to Goa tomorrow", understand they'll be away and factor that into advice)
- Keep responses SHORT — 2-4 sentences usually, unless explaining something complex
- Never repeat the same phrasing twice in a conversation

WHAT YOU ANSWER:
- Everything related to their water tank (level, usage, filling, draining, leaks, predictions)
- Water conservation tips and advice
- Water usage recommendations for their lifestyle
- General water-related questions (water quality, saving water, etc.)
- Life context that affects water (trips, guests, seasons, etc.)

WHAT YOU DON'T ANSWER:
- Anything completely unrelated to water (politics, sports, entertainment, etc.)
- For off-topic questions, kindly redirect: "I'm a water specialist — ask me about your tank or saving water instead!"

IMPORTANT — ACTIONS:
If the user wants you to do something to the tank (fill, drain, stop, fill to X%), you MUST:
1. First explain what you'll do and why
2. Ask for confirmation by ending your response with exactly this format:
CONFIRM:{{"cmd":"FILL","label":"Start filling the tank"}}
or CONFIRM:{{"cmd":"FILLTO 80","label":"Fill tank to 80%"}}
or CONFIRM:{{"cmd":"DRAIN","label":"Start draining"}}
or CONFIRM:{{"cmd":"STOP","label":"Stop the pump"}}

Never execute actions without asking first.
Never use markdown formatting like ** or ## in responses.`;
}}

function openAquaChat() {{
  showScreen('aqua');
  var msgs = document.getElementById('aqua-messages');
  if (msgs && msgs.children.length === 0) {{
    // Initial greeting based on tank status
    var greeting;
    if (!aquaTankData.connected) {{
      greeting = "Hi! I'm Aqua, your water assistant. I can answer questions about water conservation and tank management. Connect your tank via Bluetooth or WiFi to get personalized advice about your water levels!";
    }} else if (aquaTankData.leak) {{
      greeting = "Hey — heads up, I'm detecting a possible leak right now. Your level is dropping faster than normal. Check your pipes and connections. Want me to stop the pump?";
    }} else if (aquaTankData.level_pct < 15) {{
      greeting = "Hi! Quick heads up — your tank is critically low at " + Math.round(aquaTankData.level_pct) + "%. That's less than a day of water. Want me to start filling?";
    }} else if (aquaTankData.level_pct < 30) {{
      greeting = "Hey! Tank is getting low — " + Math.round(aquaTankData.level_pct) + "% with about " + (aquaTankData.days_left ? Math.round(aquaTankData.days_left) + " days" : "a few days") + " left. Anything I can help with?";
    }} else {{
      var greetings = [
        "Hey! Tank is looking good at " + Math.round(aquaTankData.level_pct) + "% — about " + (aquaTankData.days_left ? Math.round(aquaTankData.days_left) + " days" : "several days") + " of water. What's on your mind?",
        "Hi there! Your tank is at " + Math.round(aquaTankData.level_pct) + "%, all good. Ask me anything about your water.",
        "Hello! Aqua here — keeping an eye on your " + aquaTankData.tank_L + " " + aquaTankData.unit + " tank. Currently " + Math.round(aquaTankData.level_pct) + "% full. How can I help?"
      ];
      greeting = greetings[Math.floor(Math.random() * greetings.length)];
    }}
    appendAquaMsg(greeting, 'bot');
    aquaHistory.push({{role:'model', parts:[{{text:greeting}}]}});
  }}
}}

function appendAquaMsg(text, role) {{
  var msgs = document.getElementById('aqua-messages');
  if (!msgs) return;
  var div = document.createElement('div');
  div.className = role === 'bot' ? 'aqua-msg-bot' : 'aqua-msg-user';
  div.textContent = text;
  msgs.appendChild(div);
  msgs.scrollTop = msgs.scrollHeight;
}}

function showAquaTyping() {{
  var msgs = document.getElementById('aqua-messages');
  var div = document.createElement('div');
  div.className = 'aqua-typing';
  div.id = 'aqua-typing';
  div.innerHTML = '<span></span><span></span><span></span>';
  msgs.appendChild(div);
  msgs.scrollTop = msgs.scrollHeight;
}}

function hideAquaTyping() {{
  var el = document.getElementById('aqua-typing');
  if (el) el.remove();
}}

function usePill(btn) {{
  document.getElementById('aqua-pills').style.display = 'none';
  document.getElementById('aqua-input').value = btn.textContent;
  sendAqua();
}}

function showConfirm(text, action) {{
  aquaPendingAction = action;
  var confirmDiv = document.getElementById('aqua-confirm');
  var confirmText = document.getElementById('aqua-confirm-text');
  confirmDiv.style.display = 'block';
  confirmText.textContent = text;
  document.getElementById('aqua-pills').style.display = 'none';
}}

function confirmAction(yes) {{
  document.getElementById('aqua-confirm').style.display = 'none';
  if (yes && aquaPendingAction) {{
    sendCommand(aquaPendingAction);
    appendAquaMsg('Done! I\\'ve sent the command to your tank.', 'bot');
  }} else {{
    appendAquaMsg('No problem, leaving it as is.', 'bot');
  }}
  aquaPendingAction = null;
}}

async function sendAqua() {{
  var inp = document.getElementById('aqua-input');
  if (!inp) return;
  var msg = inp.value.trim();
  if (!msg) return;
  inp.value = '';
  document.getElementById('aqua-pills').style.display = 'none';
  document.getElementById('aqua-confirm').style.display = 'none';

  appendAquaMsg(msg, 'user');
  aquaHistory.push({{role:'user', parts:[{{text:msg}}]}});

  showAquaTyping();

  try {{
    var body = {{
      system_instruction: {{parts: [{{text: getAquaSystemPrompt()}}]}},
      contents: aquaHistory,
      generationConfig: {{
        temperature: 0.9,
        maxOutputTokens: 350,
        topP: 0.95
      }}
    }};

    var res = await fetch(GEMINI_URL, {{
      method: 'POST',
      headers: {{'Content-Type': 'application/json'}},
      body: JSON.stringify(body)
    }});

    var data = await res.json();
    hideAquaTyping();

    if (!res.ok) throw new Error(data.error?.message || 'API error');

    var reply = data.candidates?.[0]?.content?.parts?.[0]?.text || "Sorry, something went wrong. Try again.";

    // Check for action confirmation request
    var confirmMatch = reply.match(/CONFIRM:(\\{{[^}}]+\\}})/);
    if (confirmMatch) {{
      try {{
        var action = JSON.parse(confirmMatch[1]);
        reply = reply.replace(/CONFIRM:\\{{[^}}]+\\}}/, '').trim();
        appendAquaMsg(reply, 'bot');
        aquaHistory.push({{role:'model', parts:[{{text:reply}}]}});
        showConfirm(action.label + ' — confirm?', action.cmd);
        return;
      }} catch(e) {{}}
    }}

    aquaHistory.push({{role:'model', parts:[{{text:reply}}]}});
    appendAquaMsg(reply, 'bot');

  }} catch(err) {{
    hideAquaTyping();
    appendAquaMsg("Hmm, I couldn't connect to my brain right now. Check your internet and try again.", 'bot');
    console.error('Aqua error:', err);
  }}
}}
'''

# Insert before closing </script>
content = content.replace('</script>\n</body>', aqua_js + '\n</script>\n</body>')
print('✓ Aqua JavaScript added')

# ── 5. Wire live data updates to Aqua ──────────────────────
old_handle = 'function handleJSONMessage(msg) {'
new_handle = '''function handleJSONMessage(msg) {
  if (typeof updateAquaData === 'function') updateAquaData(msg);'''

if old_handle in content:
    content = content.replace(old_handle, new_handle)
    print('✓ Live data wired to Aqua')
else:
    print('WARNING: handleJSONMessage not found')

# Also wire cloudWS data
old_cloud_msg = 'cloudWS.onmessage = function(e) {'
new_cloud_msg = '''cloudWS.onmessage = function(e) {
    try {
      var d = JSON.parse(e.data);
      if (typeof updateAquaData === 'function') updateAquaData(d);
    } catch(x) {}'''

if old_cloud_msg in content:
    content = content.replace(old_cloud_msg, new_cloud_msg)
    print('✓ Cloud data wired to Aqua')

# ── 6. Fix goBack to handle aqua screen ────────────────────
old_goback = 'function goBack() {'
new_goback = '''function goBack() {
  if (document.getElementById('screen-aqua').classList.contains('active')) {
    showScreen('opening');
    return;
  }'''

if old_goback in content:
    content = content.replace(old_goback, new_goback)
    print('✓ Back button fixed for Aqua screen')

# ── 7. Add openAquaChat to showScreen whitelist ─────────────
# The openAquaChat function calls showScreen('aqua')
# Make sure screen-aqua is handled

# Save
open(path, 'w').write(content)
print('')
print('=' * 45)
print('ALL DONE!')
print('File size:', len(content), 'bytes')
print('=' * 45)
