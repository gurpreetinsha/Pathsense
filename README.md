
















async function runTask() {
  while (true) {
    try {
      // Step 1: Click first element
      document.evaluate(
        "/html/body/div[1]/div[6]/div/main/turbo-frame/div/react-app/div/div/div[1]/div/div/div[2]/div/div/div[3]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/a",
        document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null
      ).singleNodeValue?.click();

      // Step 2: Press spacebar
      document.dispatchEvent(new KeyboardEvent("keydown", { key: " ", code: "Space", keyCode: 32, bubbles: true }));
      document.dispatchEvent(new KeyboardEvent("keyup", { key: " ", code: "Space", keyCode: 32, bubbles: true }));

      // Step 3: Click second element
      document.evaluate(
        "/html/body/div[1]/div[6]/div/main/turbo-frame/div/react-app/div/div/div[1]/div/div/div[2]/div/div/div[3]/div[1]/div[2]/button/span/span",
        document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null
      ).singleNodeValue?.click();

      // Step 4: Click third element
      document.evaluate(
        "/html/body/div[1]/div[1]/div/div/div/div[3]/button[2]/span/span",
        document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null
      ).singleNodeValue?.click();

      // Step 5: Wait 3 seconds
      await new Promise(r => setTimeout(r, 3000));

    } catch (err) {
      console.error("Automation error:", err);
      await new Promise(r => setTimeout(r, 3000));
    }
  }
}

runTask();
  report verification system

REWARDS FOR PEOPLE
Traffic Light System: Using a green, yellow, and red/orange indicator to represent low, medium, and high levels of road threats.

Three Main Maps:

General Map: Displays overall road conditions.

Severity Map: Shows the traffic light indicators for different areas. 

Navigation Map: Provides routes tailored to the type of vehicle, filtering out lower-threat areas for vehicles like bikes.
SHAREABLE TRIP REPORT
