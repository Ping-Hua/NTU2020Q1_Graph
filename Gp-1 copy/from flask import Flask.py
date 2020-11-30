#https://medium.com/@charming_rust_oyster_221/flask-%E6%AA%94%E6%A1%88%E4%B8%8A%E5%82%B3%E5%88%B0%E4%BC%BA%E6%9C%8D%E5%99%A8%E7%9A%84%E6%96%B9%E6%B3%95-1-c11097c23137

import os
from flask import Flask, request, redirect, url_for, send_from_directory, json, render_template
from flask_assets import Bundle, Environment #bundle use to combine the file 
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = '/Users/Kyle/Desktop/Insurance Class/Upload Folder'
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

def allowed_file(filename): #篩選合格的file格式
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST']) #用來建立上傳的API
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 
                                   filename))
            return redirect(url_for('uploaded_file',filename=filename)) #當檔案上傳完，會跳轉到 uploaded_file() 函式，並帶著參數 filename
    return '''
    <!DOCTYPE html>
	<html lang="en">

	<head>
	  <meta charset="utf-8">
	  <meta content="width=device-width, initial-scale=1.0" name="viewport">

	  <title>Bar to Data Page</title>
	  <meta content="" name="descriptison">
	  <meta content="" name="keywords">

	  <!-- Favicons -->
	  <link href="assets/img/favicon.png" rel="icon">
	  <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">

	  <!-- Google Fonts -->
	  <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Raleway:300,300i,400,400i,500,500i,600,600i,700,700i|Poppins:300,300i,400,400i,500,500i,600,600i,700,700i" rel="stylesheet">

	  <!-- Vendor CSS Files -->
	  <link href="assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
	  <link href="assets/vendor/icofont/icofont.min.css" rel="stylesheet">
	  <link href="assets/vendor/boxicons/css/boxicons.min.css" rel="stylesheet">
	  <link href="assets/vendor/owl.carousel/assets/owl.carousel.min.css" rel="stylesheet">
	  <link href="assets/vendor/venobox/venobox.css" rel="stylesheet">
	  <link href="assets/vendor/remixicon/remixicon.css" rel="stylesheet">
	  <link href="assets/vendor/aos/aos.css" rel="stylesheet">

	  <!-- Template Main CSS File -->
	  <link href="assets/css/style.css" rel="stylesheet">

	  <!-- =======================================================
	  * Template Name: Gp - v2.1.0
	  * Template URL: https://bootstrapmade.com/gp-free-multipurpose-html-bootstrap-template/
	  * Author: BootstrapMade.com
	  * License: https://bootstrapmade.com/license/
	  ======================================================== -->
	</head>

	<body>

	  <!-- ======= Header ======= -->
	  <header id="header" class="fixed-top header-inner-pages">
	    <div class="container d-flex align-items-center justify-content-between">

	      <h1 class="logo"><a href="index.html">Gp<span>.</span></a></h1>
	      <!-- Uncomment below if you prefer to use an image logo -->
	      <!-- <a href="index.html" class="logo"><img src="assets/img/logo.png" alt="" class="img-fluid"></a>-->

	      <nav class="nav-menu d-none d-lg-block">
	        <ul>
	          <li class="active"><a href="/Users/Kyle/Desktop/Insurance Class/Gp-1/Main.html">Home</a></li>
	          <li><a href="#about">About</a></li>
	          <li><a href="#services">Services</a></li>
	          <li><a href="#team">Team</a></li>
	          <li class="drop-down"><a href="">Analysis</a>
	            <ul>
	              <li><a href="/Users/Kyle/Desktop/Insurance Class/Gp-1/Bar to Data Inner-Page.html">Bar Chart</a></li>
	              <li><a href="/Users/Kyle/Desktop/Insurance Class/Gp-1/Day to Data Inner Page.html">Day Chart</a></li>
	              <li><a href="/Users/Kyle/Desktop/Insurance Class/Gp-1/Line to Data Inner-Page.html">Line Chart</a></li>
	            </ul>
	          </li>
	          <li><a href="#contact">Contact</a></li>

	        </ul>
	      </nav><!-- .nav-menu -->

	      <a href="#about" class="get-started-btn scrollto">Get Started</a>

	    </div>
	  </header><!-- End Header -->

	  <main id="main">

	    <!-- ======= Breadcrumbs ======= -->
	    <section class="breadcrumbs">
	      <div class="container">

	        <div class="d-flex justify-content-between align-items-center">
	          <h2>Inner Page</h2>
	          <ol>
	            <li><a href="index.html">Home</a></li>
	            <li>Inner Page</li>
	          </ol>
	        </div>

	      </div>
	    </section><!-- End Breadcrumbs -->

	    <section class="inner-page">
	      <div class="container">
	        <p>
	          Example inner page template
	        </p>
	      </div>
	    </section>

	  </main><!-- End #main -->

	  <!-- ======= Footer ======= -->
	  <footer id="footer">
	    <div class="footer-top">
	      <div class="container">
	        <div class="row">

	          <div class="col-lg-3 col-md-6">
	            <div class="footer-info">
	              <h3>Gp<span>.</span></h3>
	              <p>
	                National Taiwan University <br>
	                Taipei, Taiwan<br><br>
	                <strong>Phone:</strong> +886 123 456 789<br>
	                <strong>Email:</strong> insuranceclass@gmail.com<br>
	              </p>
	              <div class="social-links mt-3">
	                <a href="#" class="twitter"><i class="bx bxl-twitter"></i></a>
	                <a href="#" class="facebook"><i class="bx bxl-facebook"></i></a>
	                <a href="#" class="instagram"><i class="bx bxl-instagram"></i></a>
	                <a href="#" class="google-plus"><i class="bx bxl-skype"></i></a>
	                <a href="#" class="linkedin"><i class="bx bxl-linkedin"></i></a>
	              </div>
	            </div>
	          </div>

	          <div class="col-lg-2 col-md-6 footer-links">
	            <h4>Useful Links</h4>
	            <ul>
	              <li><i class="bx bx-chevron-right"></i> <a href="#">Home</a></li>
	              <li><i class="bx bx-chevron-right"></i> <a href="#">About us</a></li>
	              <li><i class="bx bx-chevron-right"></i> <a href="#">Services</a></li>
	              <li><i class="bx bx-chevron-right"></i> <a href="#">Terms of service</a></li>
	              <li><i class="bx bx-chevron-right"></i> <a href="#">Privacy policy</a></li>
	            </ul>
	          </div>

	          <div class="col-lg-3 col-md-6 footer-links">
	            <h4>Our Services</h4>
	            <ul>
	              <li><i class="bx bx-chevron-right"></i> <a href="#"></a></li>
	              <li><i class="bx bx-chevron-right"></i> <a href="#">Web Development</a></li>
	              <li><i class="bx bx-chevron-right"></i> <a href="#">Product Management</a></li>
	              <li><i class="bx bx-chevron-right"></i> <a href="#">Marketing</a></li>
	              <li><i class="bx bx-chevron-right"></i> <a href="#">Graphic Design</a></li>
	            </ul>
	          </div>

	          <div class="col-lg-4 col-md-6 footer-newsletter">
	            <h4>Our Newsletter</h4>
	            <p>We create just for showing. Please don't expect that we may sent any newsletter</p>
	            <form action="" method="post">
	              <input type="email" name="email"><input type="submit" value="Subscribe">
	            </form>

	          </div>

	        </div>
	      </div>
	    </div>

	    <div class="container">
	      <div class="copyright">
	        &copy; Copyright <strong><span>Gp</span></strong>. All Rights Reserved
	      </div>
	      <div class="credits">
	        <!-- All the links in the footer should remain intact. -->
	        <!-- You can delete the links only if you purchased the pro version. -->
	        <!-- Licensing information: https://bootstrapmade.com/license/ -->
	        <!-- Purchase the pro version with working PHP/AJAX contact form: https://bootstrapmade.com/gp-free-multipurpose-html-bootstrap-template/ -->
	        Designed by <a href="https://bootstrapmade.com/">NTU Insurance</a>
	      </div>
	    </div>
	  </footer><!-- End Footer -->

	    <div class="container">
	      <div class="copyright">
	        &copy; Copyright <strong><span>Gp</span></strong>. All Rights Reserved
	      </div>
	      <div class="credits">
	        <!-- All the links in the footer should remain intact. -->
	        <!-- You can delete the links only if you purchased the pro version. -->
	        <!-- Licensing information: https://bootstrapmade.com/license/ -->
	        <!-- Purchase the pro version with working PHP/AJAX contact form: https://bootstrapmade.com/gp-free-multipurpose-html-bootstrap-template/ -->
	        Designed by <a href="https://bootstrapmade.com/">BootstrapMade</a>
	      </div>
	    </div>
	  </footer><!-- End Footer -->

	  <a href="#" class="back-to-top"><i class="ri-arrow-up-line"></i></a>
	  <div id="preloader"></div>

	  <!-- Vendor JS Files -->
	  <script src="assets/vendor/jquery/jquery.min.js"></script>
	  <script src="assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
	  <script src="assets/vendor/jquery.easing/jquery.easing.min.js"></script>
	  <script src="assets/vendor/php-email-form/validate.js"></script>
	  <script src="assets/vendor/owl.carousel/owl.carousel.min.js"></script>
	  <script src="assets/vendor/isotope-layout/isotope.pkgd.min.js"></script>
	  <script src="assets/vendor/venobox/venobox.min.js"></script>
	  <script src="assets/vendor/waypoints/jquery.waypoints.min.js"></script>
	  <script src="assets/vendor/counterup/counterup.min.js"></script>
	  <script src="assets/vendor/aos/aos.js"></script>

	  <!-- Template Main JS File -->
	  <script src="assets/js/main.js"></script>

	</body>

	</html>
    '''
@app.route('/uploads/<filename>') #從local回傳檔案回http://127.0.0.1:5000/uploads/<filename>
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)    #這邊的filename是我們前面先requests的檔名，用來做index找要會傳回網站的是哪個

if __name__ == '__main__':
    app.run(debug = True)   