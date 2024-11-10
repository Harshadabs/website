<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
    <title>Mumbai Hub</title>
</head>
<body>
  <div>
    <div class="nav-container">
      <header>
        <div class="logo">ArconHUB</div>
        <nav>
          <a href="index.php">Home</a>
        </nav>
        <button class="login-signup" onclick="location.href='login.php'">Login / Sign In</button>
      </header>
    </div>

    <div class="container">
        <div class="slideshow-container" style="margin-top: 3.9em;">
            <?php
            $slides = [
                ["src" => "photo scroll/balmond-bioroid-starlight-skin-mobile-legends-2k-wallpaper-uhdpaper.com-732@0@f.jpg", "text" => "Balmond"],
                ["src" => "photo scroll/dyrroth-venom-mobile-legends-skin-2k-wallpaper-uhdpaper.com-331@1@g.jpg", "text" => "Dyroth"],
                ["src" => "photo scroll/xavier-mobile-legends-2k-wallpaper-uhdpaper.com-334@1@g.jpg", "text" => "Xavier"],
            ];

            foreach ($slides as $index => $slide) {
                $num = $index + 1;
                echo "<div class='mySlides fade'>
                          <div class='numbertext'>$num / 3</div>
                          <img src='{$slide['src']}' style='width:100%'>
                          <div class='text'>{$slide['text']}</div>
                      </div>";
            }
            ?>
            
            <!-- Next and previous buttons -->
            <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
            <a class="next" onclick="plusSlides(1)">&#10095;</a>
        </div>
        
        <br>
          
        <!-- The dots/circles -->
        <div style="text-align:center">
            <?php for ($i = 1; $i <= count($slides); $i++): ?>
                <span class="dot" onclick="currentSlide(<?= $i ?>)"></span>
            <?php endfor; ?>
        </div>
   
        <div class="grid-container-home container">
            <?php
            $games = [
                ["link" => "mobilelegends.php", "img" => "photo scroll/mobile legends.png", "name" => "Moba Legends 5V5"],
                ["link" => "genshin.php", "img" => "photo scroll/Genshin_Impact.png", "name" => "Genshin Impact"],
                ["link" => "honkai star rail.php", "img" => "photo scroll/honkai star rail.avif", "name" => "Honkai Star Rail"],
                ["link" => "#", "img" => "photo scroll/clash of clans.jpg", "name" => "Clash of Clans", "tag" => "Coming soon !"]
            ];

            foreach ($games as $game) {
                echo "<div class='card grid-item'>
                          <a href='{$game['link']}' class='Item__link'>
                            <div class='product-container'>
                              <img src='{$game['img']}' alt='{$game['name']}' class='image'>
                            </div>";
                if (isset($game['tag'])) {
                    echo "<span class='tag display-topleft coc'>{$game['tag']}</span>";
                }
                echo "<span class='Item__price'>{$game['name']}</span>
                          </a>
                      </div>";
            }
            ?>
        </div>
    </div>
  </div>

<script>
let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}
</script>
</body>
</html>
