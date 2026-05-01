<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tip Calculator</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <div class="container">
        <h2>Tip Calculator</h2>

        <label>Total Bill ($)</label>
        <input type="number" id="bill" placeholder="Enter bill amount">

        <label>Tip Percentage (%)</label>
        <input type="number" id="tip" placeholder="10, 12, 15...">

        <label>Number of People</label>
        <input type="number" id="people" placeholder="Enter number of people">

        <button onclick="calculateTip()">Calculate</button>

        <h3 id="result"></h3>
    </div>

<script src="script.js"></script>
</body>
</html>

