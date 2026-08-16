import os
import json

# 1. Force Python to use the exact folder where this script is located
current_folder = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(current_folder, "index.html")
json_path = os.path.join(current_folder, "data.json")

# 2. The exact, error-free HTML code
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1, user-scalable=no">
<title>The Anchor</title>
<style>
  :root {
    --bg-color: #050505;
    --text-color: #d1d1d1;
  }
  * { box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
  body, html {
    background-color: var(--bg-color);
    margin: 0; padding: 0; height: 100vh; width: 100vw;
    display: flex; justify-content: center; align-items: center;
    cursor: pointer; overflow: hidden;
  }
  .text-container { width: 85%; max-width: 600px; text-align: center; }
  .statement {
    font-family: 'Georgia', serif; font-size: 22px; line-height: 1.6;
    color: var(--text-color); opacity: 0; transform: translateY(10px);
    transition: opacity 1.5s ease, transform 1.5s ease;
  }
  .statement.visible { opacity: 1; transform: translateY(0); }
</style>
</head>
<body>
  <div class="text-container">
    <div class="statement" id="statementText">Tap anywhere.</div>
  </div>
<script>
  let statements = { morning: [], afternoon: [], evening: [] };
  const textElement = document.getElementById('statementText');
  let isAnimating = false;

  fetch('data.json')
    .then(response => response.json())
    .then(data => {
      statements = data;
      textElement.classList.add('visible');
    })
    .catch(error => {
      textElement.textContent = "System ready. Tap to begin.";
      textElement.classList.add('visible');
    });

  function getCategoryByTime() {
    const hour = new Date().getHours();
    if (hour >= 5 && hour < 13) return statements.morning;
    if (hour >= 13 && hour < 18) return statements.afternoon;
    return statements.evening;
  }

  document.body.addEventListener('click', () => {
    if (isAnimating) return;
    isAnimating = true;
    textElement.classList.remove('visible');

    setTimeout(() => {
      const currentCategory = getCategoryByTime();
      if (currentCategory && currentCategory.length > 0) {
        const randomIndex = Math.floor(Math.random() * currentCategory.length);
        textElement.textContent = currentCategory[randomIndex];
      }
      textElement.classList.add('visible');
      isAnimating = false;
    }, 1500);
  });
</script>
</body>
</html>
"""

# 3. The baseline database of Area Manager and life triage statements
json_data = {
  "morning": [
    "SOCIAL AUTOPILOT: 'The flight was straightforward. How is the construction sector moving here this quarter?' Say it, nod, and let them talk.",
    "The meeting in Egypt is an exchange of technical information, not a performance. State the Penetron data, answer the questions, and the interaction is successful.",
    "LOGISTICAL TRIAGE: Coordinating the single car today is just a scheduling variable. Solve the math with your wife for the next 24 hours and ignore the rest.",
    "You are the Area Manager. You dictate the regional targets. Do not let Lyzan Co. or any distributor make you feel like you are working for them.",
    "A WhatsApp message from a contractor at 8:00 AM is their emergency, not yours. Triage the problem. Is it a leak, or is it panic? Treat the leak; ignore the panic.",
    "You do not need to be the loudest person in the executive session. Technical superiority and quiet confidence close the deal."
  ],
  "afternoon": [
    "NOISE CANCELLER: The people projecting negativity are not paying your bills or raising your children. Their words have zero bearing capacity on your life.",
    "An introvert's energy is a finite currency. Stop spending it trying to convince contractors who are committed to cutting corners.",
    "If a project in Basra or Baghdad is leaking right now, you cannot fix it by stressing from Sulaymaniyah. Request the photos, analyze the routing, and send the Penecrete protocol.",
    "You are 37. The heavy lifting you are doing now across these regions is buying the stability of your 50s. The crushing weight is temporary.",
    "Step away from the screen for sixty seconds. Visualize the Sicilian Defense. Map the board in your head. Give your analytical brain a break from the construction data.",
    "A distributor's lack of planning does not constitute your emergency. Set the boundary and hold the line."
  ],
  "evening": [
    "GHOST OBLIGATION: The digital keyboard is silent tonight. That is fine. It is waiting for you, not judging you. Release the guilt.",
    "Leave the Area Manager mindset at the door. Hano and Evie do not need a geotechnical expert or a boss. They just need their father.",
    "GHOST OBLIGATION: The books by Murakami and Dostoevsky are an escape, not an assignment. There is no deadline for reading. If you are too tired, rest your eyes.",
    "Your wife is your partner in this, not another obligation. Share the weight of the day with her, even if it is just sitting in silence together.",
    "The house is quiet. The work is done. You are safe. Allow yourself to actually inhabit this moment without projecting into the future.",
    "Tomorrow's problems belong to tomorrow. You cannot solve them tonight. Close the mental tabs."
  ]
}

# 4. Create the files automatically in the forced location
print(f"Building The Anchor directly in: {current_folder}")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)
print("✓ index.html created successfully.")

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(json_data, f, indent=2, ensure_ascii=False)
print("✓ data.json created successfully.")

print("\nAll files generated perfectly in the correct folder. You are ready to upload to GitHub.")