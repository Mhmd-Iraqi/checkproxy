</html>
<html>
   <head> <title>MHMD TOOLS</title>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
      <script src="https://kit.fontawesome.com/55db5a83a3.js" crossorigin="anonymous"></script>
      <style>
         .btn {
         background-color:white;
         color: #FF0000;
         border-radius:10px;
         border:double;
         }
      .form-control {
         background-color:white;
         color: #FF0000;
         border-radius:10px;
         border:double;
         }
      </style>
   </head>
   <body>
<?php

error_reporting(0);
if(isset($_GET['submit'])){

$proxy=$_GET['proxy'];
$ch = curl_init();
$data ="data=".$proxy;
curl_setopt($ch, CURLOPT_URL, "https://hidemy.name/api/checker.php?out=js&action=list_new&tasks=http,ssl,socks4,socks5&parser=lines");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, $data);
//curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_ENCODING, "gzip");
$result = curl_exec($ch);
curl_close($ch);

$api = json_decode($result, true);
 echo "<div class='success'><center>
 <font color='blue'><hr>$result<hr></font></center></div>";
	    };
if(!isset($_GET['submit'])){
	?>
	<section>
		<div class="container p-5 ">
			<form action="" method="get">
				<div class="mb-3">
					<label class="form-label">Proxy</label>
					<input type='text' name='proxy' class="form-control" required>

					
				
					
				</div>
				<button type="submit" name='submit' value='submit' class="btn btn-primary">Submit</button>
				
			</form>
			
		</div>
		
	</section>
	<?php
	}
	
	?>
	<section>
		<div class="container p-2 text-center">
 <div id="formFooter">
        <a class="underlineHover" href="https://www.instagram.com/4e_m1">Instagram</a>
 <div id="formFooter">
        <a class="underlineHover" href="https://t.me/J_W_2">Programing</a>
  <div id="formFooter">
  	<a class="underlineHover" href="https://t.me/toolfile">Ch Programing</a>
      </div>
      </div>
			
		</div>
		
	</section>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
	
  </body>
  
</html>
					
