<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="game page.css">
    <title>Honkai Star Rail</title>
</head>
<body>

    <div class="nav-container">
      <header>
        <div class="logo">ArconHUB</div>
        <nav>
            <a href="index.php">HOME</a>
        </nav>
        <nav>
            <a href="login.php" class="login-signup">LOGIN / SIGN UP</a>
        </nav>  
      </header>
    </div>

    <div class="container">
        <img src="photo scroll/hsr logo.jpg" alt="Honkai Star Rail" width="200px" class="game-image">
        <div class="instructions">
            <h3>How to Top Up Honkai Star Rail Oneiric Shards:</h3>
            <ol>
                <li>Enter ID & select Server</li>
                <li>Select grid-item</li>
                <li>Select Payment</li>
                <li>Enter WhatsApp No</li>
                <li>Click Confirm Top Up & make Payment</li>
                <li>Oneiric shards are automatically transferred to your game account</li>
            </ol>
        </div>

        <div class="section">
            <div class="sidebar">
                <h3>1.) Input Data Game</h3>
                <div class="input-row">
                    <input type="number" name="user_id" required placeholder="Input User ID" class="input-box">
                    <select class="input-box">
                        <option>Select Server</option>
                        <option>Asia</option>
                        <option>Europe</option>
                        <option>America</option>
                        <option>Tw,Hk,Mo</option>
                    </select>
                </div>        
            </div>
            <p class="instruction">
                Please enter your User ID & Server and make sure it is correct. Example: 123456789 | server-asia.
            </p>
        </div>

        <h3>2.) Select Service Amount</h3>

        <div class="Items grid-container">
            <?php
            // Define items for dynamic rendering
            $items = [
                ["amount" => "60", "price" => "₹ 95"],
                ["amount" => "330", "price" => "₹ 400"],
                ["amount" => "1090", "price" => "₹ 1200"],
                ["amount" => "2240", "price" => "₹ 2500"],
                ["amount" => "3880", "price" => "₹ 3800"],
                ["amount" => "8080", "price" => "₹ 7500"],
                ["amount" => "express supply pass", "price" => "₹ 400"],
            ];

            foreach ($items as $item) {
                echo "<button class='box grid-item'>
                        <a href='#' class='Item__link'>
                            <div class='product-container' style='display: block;'>
                                <img src='photo scroll/shards.png' alt='Oneiric Shard' class='Image'>
                                <span class='Item__title'>{$item['amount']}</span>
                            </div>
                            <span class='Item__price'>{$item['price']}</span>
                        </a>
                      </button>";
            }
            ?>
        </div>
      
    </div>
</body>
<script>
document.querySelectorAll('.grid-item').forEach(item => {
    item.addEventListener('click', function() {
        // Remove active class from all grid items
        document.querySelectorAll('.grid-item').forEach(el => el.classList.remove('active'));

        // Add active class to the clicked item
        this.classList.add('active');
    });
});
</script>
</html>
