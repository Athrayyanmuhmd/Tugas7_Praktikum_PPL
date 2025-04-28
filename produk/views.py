from django.http import HttpResponse

# Data dummy untuk produk
daftar_produk = [
    {
        'id': 1,
        'nama': 'Laptop Gaming',
        'deskripsi': 'Laptop gaming dengan spesifikasi tinggi',
        'harga': 15000000,
        'stok': 10,
        'gambar': 'laptop.jpg'
    },
    {
        'id': 2,
        'nama': 'Smartphone',
        'deskripsi': 'Smartphone dengan kamera terbaik',
        'harga': 8000000,
        'stok': 15,
        'gambar': 'smartphone.jpg'
    },
    {
        'id': 3,
        'nama': 'Headphone',
        'deskripsi': 'Headphone dengan noise cancelling',
        'harga': 2000000,
        'stok': 20,
        'gambar': 'headphone.jpg'
    },
    {
        'id': 4,
        'nama': 'Monitor Gaming',
        'deskripsi': 'Monitor gaming 144Hz',
        'harga': 3500000,
        'stok': 5,
        'gambar': 'monitor.jpg'
    },
    {
        'id': 5,
        'nama': 'Keyboard Mechanical',
        'deskripsi': 'Keyboard mechanical dengan RGB',
        'harga': 1200000,
        'stok': 25,
        'gambar': 'keyboard.jpg'
    }
]

def home(request):
    """View untuk halaman home (/)"""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>TechVision - Katalog Produk Elektronik</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
        <style>
            :root {
                --primary-color: #4361ee;
                --secondary-color: #3f37c9;
                --accent-color: #f72585;
                --bg-color: #f8f9fa;
                --text-color: #333;
                --light-text: #6c757d;
                --white: #ffffff;
                --shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                --transition: all 0.3s ease;
            }
            
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Poppins', sans-serif;
                line-height: 1.6;
                color: var(--text-color);
                background-color: var(--bg-color);
                overflow-x: hidden;
            }
            
            header {
                background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
                padding: 1.5rem 0;
                position: sticky;
                top: 0;
                z-index: 100;
                box-shadow: var(--shadow);
            }
            
            .navbar {
                display: flex;
                justify-content: space-between;
                align-items: center;
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 20px;
            }
            
            .logo {
                font-size: 1.8rem;
                font-weight: 700;
                color: var(--white);
                text-decoration: none;
            }
            
            .nav-links {
                display: flex;
                gap: 2rem;
            }
            
            .nav-links a {
                color: var(--white);
                text-decoration: none;
                font-weight: 500;
                font-size: 1.1rem;
                transition: var(--transition);
                position: relative;
            }
            
            .nav-links a:after {
                content: '';
                position: absolute;
                width: 0;
                height: 2px;
                bottom: -5px;
                left: 0;
                background-color: var(--white);
                transition: var(--transition);
            }
            
            .nav-links a:hover:after {
                width: 100%;
            }
            
            .hero {
                height: 80vh;
                background: url('https://images.unsplash.com/photo-1550009158-9ebf69173e03?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80') no-repeat center center/cover;
                position: relative;
                display: flex;
                align-items: center;
                justify-content: center;
                text-align: center;
                color: var(--white);
            }
            
            .hero:before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0, 0, 0, 0.5);
            }
            
            .hero-content {
                max-width: 800px;
                padding: 2rem;
                position: relative;
                z-index: 1;
            }
            
            .hero h1 {
                font-size: 3.5rem;
                margin-bottom: 1.5rem;
                font-weight: 700;
            }
            
            .hero p {
                font-size: 1.2rem;
                margin-bottom: 2rem;
            }
            
            .btn {
                display: inline-block;
                background-color: var(--accent-color);
                color: var(--white);
                padding: 12px 30px;
                border-radius: 50px;
                text-decoration: none;
                font-weight: 600;
                transition: var(--transition);
                border: none;
                cursor: pointer;
                box-shadow: var(--shadow);
            }
            
            .btn:hover {
                transform: translateY(-3px);
                box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
            }
            
            .container {
                max-width: 1200px;
                margin: 5rem auto;
                padding: 0 20px;
            }
            
            .section-title {
                text-align: center;
                margin-bottom: 3rem;
                position: relative;
            }
            
            .section-title h2 {
                font-size: 2.5rem;
                font-weight: 700;
                margin-bottom: 1rem;
                color: var(--secondary-color);
            }
            
            .section-title:after {
                content: '';
                position: absolute;
                width: 100px;
                height: 3px;
                background-color: var(--accent-color);
                bottom: -10px;
                left: 50%;
                transform: translateX(-50%);
            }
            
            .features {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 2rem;
                margin-top: 3rem;
            }
            
            .feature-card {
                background-color: var(--white);
                border-radius: 10px;
                padding: 2rem;
                text-align: center;
                box-shadow: var(--shadow);
                transition: var(--transition);
            }
            
            .feature-card:hover {
                transform: translateY(-10px);
                box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
            }
            
            .feature-card i {
                font-size: 3rem;
                color: var(--primary-color);
                margin-bottom: 1.5rem;
            }
            
            .feature-card h3 {
                font-size: 1.5rem;
                margin-bottom: 1rem;
                color: var(--secondary-color);
            }
            
            .feature-icon {
                width: 80px;
                height: 80px;
                margin: 0 auto 1.5rem;
                background-color: rgba(67, 97, 238, 0.1);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 2rem;
                color: var(--primary-color);
            }
            
            .cta-section {
                background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
                padding: 5rem 0;
                text-align: center;
                color: var(--white);
                margin-top: 5rem;
            }
            
            .cta-content {
                max-width: 800px;
                margin: 0 auto;
            }
            
            .cta-section h2 {
                font-size: 2.5rem;
                margin-bottom: 1.5rem;
            }
            
            .cta-section p {
                font-size: 1.2rem;
                margin-bottom: 2rem;
            }
            
            .cta-btn {
                background-color: var(--white);
                color: var(--primary-color);
            }
            
            footer {
                background-color: #222;
                color: var(--white);
                padding: 3rem 0;
            }
            
            .footer-content {
                max-width: 1200px;
                margin: 0 auto;
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 2rem;
                padding: 0 20px;
            }
            
            .footer-column h3 {
                font-size: 1.5rem;
                margin-bottom: 1.5rem;
                position: relative;
                padding-bottom: 10px;
            }
            
            .footer-column h3:after {
                content: '';
                position: absolute;
                width: 50px;
                height: 2px;
                background-color: var(--accent-color);
                bottom: 0;
                left: 0;
            }
            
            .footer-column p, .footer-column a {
                color: #aaa;
                margin-bottom: 10px;
                display: block;
                text-decoration: none;
                transition: var(--transition);
            }
            
            .footer-column a:hover {
                color: var(--white);
                padding-left: 5px;
            }
            
            .copyright {
                text-align: center;
                padding-top: 2rem;
                margin-top: 2rem;
                border-top: 1px solid #444;
                color: #aaa;
            }
            
            /* Responsive styles */
            @media (max-width: 768px) {
                .hero h1 {
                    font-size: 2.5rem;
                }
                
                .section-title h2 {
                    font-size: 2rem;
                }
                
                .cta-section h2 {
                    font-size: 2rem;
                }
                
                .nav-links {
                    gap: 1rem;
                }
            }
        </style>
    </head>
    <body>
        <header>
            <div class="navbar">
                <a href="/" class="logo">TechVision</a>
                <div class="nav-links">
                    <a href="/">Home</a>
                    <a href="/produk/">Produk</a>
                    <a href="/tentang/">Tentang</a>
                    <a href="/kontak/">Kontak</a>
                </div>
            </div>
        </header>
        
        <section class="hero">
            <div class="hero-content">
                <h1>Teknologi Terkini untuk Kehidupan Modern</h1>
                <p>Temukan koleksi produk elektronik premium kami dengan teknologi terbaru dan desain yang elegan</p>
                <a href="/produk/" class="btn">Jelajahi Produk</a>
            </div>
        </section>
        
        <div class="container">
            <div class="section-title">
                <h2>Mengapa Memilih Kami?</h2>
                <p>Kami menawarkan produk terbaik dengan layanan premium</p>
            </div>
            
            <div class="features">
                <div class="feature-card">
                    <div class="feature-icon">★</div>
                    <h3>Kualitas Premium</h3>
                    <p>Semua produk kami melewati uji kualitas ketat untuk memastikan kepuasan pelanggan.</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-icon">⚡</div>
                    <h3>Pengiriman Cepat</h3>
                    <p>Nikmati layanan pengiriman cepat ke seluruh Indonesia dengan jaminan keamanan produk.</p>
                </div>
                
                <div class="feature-card">
                    <div class="feature-icon">♻</div>
                    <h3>Garansi Resmi</h3>
                    <p>Semua produk dilengkapi dengan garansi resmi dan layanan purna jual terpercaya.</p>
                </div>
            </div>
        </div>
        
        <section class="cta-section">
            <div class="cta-content">
                <h2>Siap Meningkatkan Gaya Hidup Digital Anda?</h2>
                <p>Jelajahi koleksi lengkap produk elektronik premium kami dan temukan yang sesuai dengan kebutuhan Anda.</p>
                <a href="/produk/" class="btn cta-btn">Lihat Semua Produk</a>
            </div>
        </section>
        
        <footer>
            <div class="footer-content">
                <div class="footer-column">
                    <h3>TechVision</h3>
                    <p>Menyediakan produk elektronik premium dengan teknologi terkini untuk mengoptimalkan gaya hidup digital Anda.</p>
                </div>
                
                <div class="footer-column">
                    <h3>Link Cepat</h3>
                    <a href="/">Home</a>
                    <a href="/produk/">Produk</a>
                    <a href="/tentang/">Tentang Kami</a>
                    <a href="/kontak/">Kontak</a>
                </div>
                
                <div class="footer-column">
                    <h3>Kontak</h3>
                    <p>Jl. Lambhuk No. 123, Banda Aceh</p>
                    <p>Beyond.com</p>
                    <p>(021) 123-4567</p>
                </div>
                
                <div class="footer-column">
                    <h3>Jam Operasional</h3>
                    <p>Senin - Jumat: 08:00 - 17:00</p>
                    <p>Sabtu: 09:00 - 15:00</p>
                    <p>Minggu: Tutup</p>
                </div>
            </div>
            
            <div class="copyright">
                <p>&copy; 2025 TechVision. All Rights Reserved.</p>
            </div>
        </footer>
    </body>
    </html>
    """
    return HttpResponse(html_content)

def daftar_produk_view(request):
    """View untuk halaman daftar produk (/produk/)"""
    
    # Gambar placeholder untuk produk
    product_images = [
        "https://via.placeholder.com/300x200/4361ee/ffffff?text=Laptop+Gaming",
        "https://via.placeholder.com/300x200/3a0ca3/ffffff?text=Smartphone",
        "https://via.placeholder.com/300x200/4895ef/ffffff?text=Headphone",
        "https://via.placeholder.com/300x200/4cc9f0/ffffff?text=Monitor",
        "https://via.placeholder.com/300x200/560bad/ffffff?text=Keyboard"
    ]
    
    # Membuat HTML untuk daftar produk
    produk_items = ""
    for i, produk in enumerate(daftar_produk):
        img_src = product_images[i] if i < len(product_images) else "https://via.placeholder.com/300x200/4361ee/ffffff?text=Product"
        
        produk_items += f"""
        <div class="product-card">
            <div class="product-image">
                <img src="{img_src}" alt="{produk['nama']}">
                <div class="product-tag">Terlaris</div>
            </div>
            <div class="product-info">
                <h3>{produk['nama']}</h3>
                <div class="product-rating">
                    <span>★★★★</span><span class="light-star">★</span>
                    <span class="review-count">(120)</span>
                </div>
                <p class="product-desc">{produk['deskripsi']}</p>
                <div class="product-price-stock">
                    <p class="price">Rp {produk['harga']:,}</p>
                    <p class="stock">Stok: {produk['stok']}</p>
                </div>
                <a href="/produk/{produk['id']}/" class="btn-detail">Lihat Detail</a>
            </div>
        </div>
        """
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Katalog Produk - TechVision</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
        <style>
            :root {{
                --primary-color: #4361ee;
                --secondary-color: #3f37c9;
                --accent-color: #f72585;
                --bg-color: #f8f9fa;
                --text-color: #333;
                --light-text: #6c757d;
                --white: #ffffff;
                --shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                --transition: all 0.3s ease;
                --gray-100: #f8f9fa;
                --gray-200: #e9ecef;
                --gray-300: #dee2e6;
            }}
            
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            
            body {{
                font-family: 'Poppins', sans-serif;
                line-height: 1.6;
                color: var(--text-color);
                background-color: var(--bg-color);
                overflow-x: hidden;
            }}
            
            header {{
                background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
                padding: 1.5rem 0;
                position: sticky;
                top: 0;
                z-index: 100;
                box-shadow: var(--shadow);
            }}
            
            .navbar {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 20px;
            }}
            
            .logo {{
                font-size: 1.8rem;
                font-weight: 700;
                color: var(--white);
                text-decoration: none;
            }}
            
            .nav-links {{
                display: flex;
                gap: 2rem;
            }}
            
            .nav-links a {{
                color: var(--white);
                text-decoration: none;
                font-weight: 500;
                font-size: 1.1rem;
                transition: var(--transition);
                position: relative;
            }}
            
            .nav-links a:after {{
                content: '';
                position: absolute;
                width: 0;
                height: 2px;
                bottom: -5px;
                left: 0;
                background-color: var(--white);
                transition: var(--transition);
            }}
            
            .nav-links a:hover:after {{
                width: 100%;
            }}
            
            .page-header {{
                background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
                padding: 3rem 0;
                color: var(--white);
                text-align: center;
                margin-bottom: 3rem;
            }}
            
            .page-header h1 {{
                font-size: 2.5rem;
                margin-bottom: 1rem;
            }}
            
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 20px;
            }}
            
            .product-filter {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 2rem;
                background-color: var(--white);
                padding: 1rem 1.5rem;
                border-radius: 8px;
                box-shadow: var(--shadow);
            }}
            
            .filter-options {{
                display: flex;
                gap: 1rem;
            }}
            
            .filter-options select {{
                padding: 8px 16px;
                border: 1px solid var(--gray-300);
                border-radius: 4px;
                font-family: 'Poppins', sans-serif;
                cursor: pointer;
            }}
            
            .search-box {{
                display: flex;
            }}
            
            .search-box input {{
                padding: 8px 16px;
                border: 1px solid var(--gray-300);
                border-radius: 4px 0 0 4px;
                font-family: 'Poppins', sans-serif;
                width: 250px;
            }}
            
            .search-box button {{
                background-color: var(--primary-color);
                color: var(--white);
                border: none;
                border-radius: 0 4px 4px 0;
                padding: 0 15px;
                cursor: pointer;
            }}
            
            .products-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
                gap: 2rem;
            }}
            
            .product-card {{
                background-color: var(--white);
                border-radius: 8px;
                overflow: hidden;
                box-shadow: var(--shadow);
                transition: var(--transition);
            }}
            
            .product-card:hover {{
                transform: translateY(-10px);
                box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
            }}
            
            .product-image {{
                position: relative;
            }}
            
            .product-image img {{
                width: 100%;
                height: 200px;
                object-fit: cover;
                display: block;
            }}
            
            .product-tag {{
                position: absolute;
                top: 10px;
                right: 10px;
                background-color: var(--accent-color);
                color: var(--white);
                padding: 5px 10px;
                border-radius: 4px;
                font-size: 0.8rem;
                font-weight: 600;
            }}
            
            .product-info {{
                padding: 1.5rem;
            }}
            
            .product-info h3 {{
                font-size: 1.3rem;
                margin-bottom: 0.75rem;
                color: var(--text-color);
            }}
            
            .product-rating {{
                color: #ffc107;
                margin-bottom: 0.75rem;
                display: flex;
                align-items: center;
            }}
            
            .light-star {{
                color: #e9ecef;
            }}
            
            .review-count {{
                color: var(--light-text);
                margin-left: 5px;
                font-size: 0.9rem;
            }}
            
            .product-desc {{
                font-size: 0.9rem;
                color: var(--light-text);
                margin-bottom: 1rem;
                height: 60px;
                overflow: hidden;
                text-overflow: ellipsis;
                display: -webkit-box;
                -webkit-line-clamp: 2;
                -webkit-box-orient: vertical;
            }}
            
            .product-price-stock {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 1rem;
            }}
            
            .price {{
                font-size: 1.3rem;
                font-weight: 700;
                color: var(--accent-color);
            }}
            
            .stock {{
                font-size: 0.9rem;
                color: var(--light-text);
            }}
            
            .btn-detail {{
                display: block;
                width: 100%;
                background-color: var(--primary-color);
                color: var(--white);
                text-decoration: none;
                text-align: center;
                padding: 10px 0;
                border-radius: 4px;
                font-weight: 600;
                transition: var(--transition);
            }}
            
            .btn-detail:hover {{
                background-color: var(--secondary-color);
            }}
            
            .pagination {{
                display: flex;
                justify-content: center;
                margin: 3rem 0;
            }}
            
            .pagination a {{
                display: flex;
                justify-content: center;
                align-items: center;
                width: 40px;
                height: 40px;
                margin: 0 5px;
                background-color: var(--white);
                color: var(--text-color);
                text-decoration: none;
                border-radius: 50%;
                font-weight: 500;
                transition: var(--transition);
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }}
            
            .pagination a:hover, .pagination a.active {{
                background-color: var(--primary-color);
                color: var(--white);
            }}
            
            footer {{
                background-color: #222;
                color: var(--white);
                padding: 3rem 0;
                margin-top: 5rem;
            }}
            
            .footer-content {{
                max-width: 1200px;
                margin: 0 auto;
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 2rem;
                padding: 0 20px;
            }}
            
            .footer-column h3 {{
                font-size: 1.5rem;
                margin-bottom: 1.5rem;
                position: relative;
                padding-bottom: 10px;
            }}
            
            .footer-column h3:after {{
                content: '';
                position: absolute;
                width: 50px;
                height: 2px;
                background-color: var(--accent-color);
                bottom: 0;
                left: 0;
            }}
            
            .footer-column p, .footer-column a {{
                color: #aaa;
                margin-bottom: 10px;
                display: block;
                text-decoration: none;
                transition: var(--transition);
            }}
            
            .footer-column a:hover {{
                color: var(--white);
                padding-left: 5px;
            }}
            
            .copyright {{
                text-align: center;
                padding-top: 2rem;
                margin-top: 2rem;
                border-top: 1px solid #444;
                color: #aaa;
            }}
            
            /* Responsive styles */
            @media (max-width: 768px) {{
                .product-filter {{
                    flex-direction: column;
                    align-items: stretch;
                    gap: 1rem;
                }}
                
                .filter-options {{
                    flex-wrap: wrap;
                }}
                
                .search-box input {{
                    width: 100%;
                }}
                
                .search-box {{
                    width: 100%;
                }}
                
                .page-header h1 {{
                    font-size: 2rem;
                }}
            }}
        </style>
    </head>
    <body>
        <header>
            <div class="navbar">
                <a href="/" class="logo">TechVision</a>
                <div class="nav-links">
                    <a href="/">Home</a>
                    <a href="/produk/">Produk</a>
                    <a href="/tentang/">Tentang</a>
                    <a href="/kontak/">Kontak</a>
                </div>
            </div>
        </header>
        
        <div class="page-header">
            <div class="container">
                <h1>Katalog Produk</h1>
                <p>Temukan produk elektronik premium dengan teknologi terkini</p>
            </div>
        </div>
        
        <div class="container">
            <div class="product-filter">
                <div class="filter-options">
                    <select name="category">
                        <option value="">Semua Kategori</option>
                        <option value="laptop">Laptop</option>
                        <option value="smartphone">Smartphone</option>
                        <option value="accessories">Aksesoris</option>
                    </select>
                    
                    <select name="sort">
                        <option value="popular">Paling Populer</option>
                        <option value="newest">Terbaru</option>
                        <option value="price_low">Harga: Rendah ke Tinggi</option>
                        <option value="price_high">Harga: Tinggi ke Rendah</option>
                    </select>
                </div>
                
                <div class="search-box">
                    <input type="text" placeholder="Cari produk...">
                    <button>🔍</button>
                </div>
            </div>
            
            <div class="products-grid">
                {produk_items}
            </div>
            
            <div class="pagination">
                <a href="#" class="active">1</a>
                <a href="#">2</a>
                <a href="#">3</a>
                <a href="#">›</a>
            </div>
        </div>
        
        <footer>
            <div class="footer-content">
                <div class="footer-column">
                    <h3>TechVision</h3>
                    <p>Menyediakan produk elektronik premium dengan teknologi terkini untuk mengoptimalkan gaya hidup digital Anda.</p>
                </div>
                
                <div class="footer-column">
                    <h3>Link Cepat</h3>
                    <a href="/">Home</a>
                    <a href="/produk/">Produk</a>
                    <a href="/tentang/">Tentang Kami</a>
                    <a href="/kontak/">Kontak</a>
                </div>
                
                <div class="footer-column">
                    <h3>Kontak</h3>
                    <p>Jl. Contoh No. 123, Jakarta</p>
                    <p>info@techvision.com</p>
                    <p>(021) 123-4567</p>
                </div>
                
                <div class="footer-column">
                    <h3>Jam Operasional</h3>
                    <p>Senin - Jumat: 08:00 - 17:00</p>
                    <p>Sabtu: 09:00 - 15:00</p>
                    <p>Minggu: Tutup</p>
                </div>
            </div>
            
            <div class="copyright">
                <p>&copy; 2025 TechVision. All Rights Reserved.</p>
            </div>
        </footer>
    </body>
    </html>
    """
    return HttpResponse(html_content)

def detail_produk(request, id_produk):
    """View untuk halaman detail produk (/produk/{id}/)"""
    # Cari produk berdasarkan ID
    produk = None
    for p in daftar_produk:
        if p['id'] == id_produk:
            produk = p
            break
    
    # Jika produk tidak ditemukan
    if produk is None:
        return HttpResponse("Produk tidak ditemukan", status=404)
    
    # Gambar placeholder sesuai produk
    product_images = {
        1: "https://via.placeholder.com/800x600/4361ee/ffffff?text=Laptop+Gaming",
        2: "https://via.placeholder.com/800x600/3a0ca3/ffffff?text=Smartphone",
        3: "https://via.placeholder.com/800x600/4895ef/ffffff?text=Headphone",
        4: "https://via.placeholder.com/800x600/4cc9f0/ffffff?text=Monitor",
        5: "https://via.placeholder.com/800x600/560bad/ffffff?text=Keyboard"
    }
    
    # Thumbnails
    thumbnails = [product_images.get(produk['id'], "https://via.placeholder.com/150x150/4361ee/ffffff?text=Preview")]
    thumbnails += [f"https://via.placeholder.com/150x150/{color}/ffffff?text=View{i}" 
                  for i, color in enumerate(["4361ee", "3a0ca3", "4895ef", "4cc9f0"], 1)]
    
    # Buat string HTML untuk thumbnails
    thumbnails_html = ""
    for i, thumb in enumerate(thumbnails):
        active_class = "active" if i == 0 else ""
        thumbnails_html += f"""
        <div class="thumbnail {active_class}">
            <img src="{thumb}" alt="Preview {i+1}">
        </div>
        """
    
    # Fitur produk
    features_list = ""
    if produk['id'] == 1:  # Laptop Gaming
        features = ["Prosesor Intel Core i9", "RAM 32GB DDR4", "SSD 1TB", "Nvidia RTX 4080", "Layar 17.3 inch 144Hz"]
    elif produk['id'] == 2:  # Smartphone
        features = ["Prosesor Snapdragon 8 Gen 2", "RAM 12GB", "Storage 256GB", "Kamera 108MP", "Baterai 5000mAh"]
    elif produk['id'] == 3:  # Headphone
        features = ["Noise Cancelling", "Bluetooth 5.2", "Baterai 30 jam", "Driver 40mm", "Mikrofon HD"]
    elif produk['id'] == 4:  # Monitor
        features = ["Layar 27 inch", "Resolution 2K QHD", "Refresh Rate 144Hz", "Response Time 1ms", "AMD FreeSync"]
    elif produk['id'] == 5:  # Keyboard
        features = ["Switch Mechanical Blue", "RGB Lighting", "Tahan Air", "Anti-ghosting", "Hotswap"]
    else:
        features = ["Fitur 1", "Fitur 2", "Fitur 3", "Fitur 4", "Fitur 5"]
    
    for feature in features:
        features_list += f"<li>✓ {feature}</li>"
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{produk['nama']} - TechVision</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
        <style>
            :root {{
                --primary-color: #4361ee;
                --secondary-color: #3f37c9;
                --accent-color: #f72585;
                --bg-color: #f8f9fa;
                --text-color: #333;
                --light-text: #6c757d;
                --white: #ffffff;
                --shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                --transition: all 0.3s ease;
                --gray-100: #f8f9fa;
                --gray-200: #e9ecef;
                --gray-300: #dee2e6;
                --gray-400: #ced4da;
                --gray-500: #adb5bd;
            }}
            
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            
            body {{
                font-family: 'Poppins', sans-serif;
                line-height: 1.6;
                color: var(--text-color);
                background-color: var(--bg-color);
                overflow-x: hidden;
            }}
            
            header {{
                background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
                padding: 1.5rem 0;
                position: sticky;
                top: 0;
                z-index: 100;
                box-shadow: var(--shadow);
            }}
            
            .navbar {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 20px;
            }}
            
            .logo {{
                font-size: 1.8rem;
                font-weight: 700;
                color: var(--white);
                text-decoration: none;
            }}
            
            .nav-links {{
                display: flex;
                gap: 2rem;
            }}
            
            .nav-links a {{
                color: var(--white);
                text-decoration: none;
                font-weight: 500;
                font-size: 1.1rem;
                transition: var(--transition);
                position: relative;
            }}
            
            .nav-links a:after {{
                content: '';
                position: absolute;
                width: 0;
                height: 2px;
                bottom: -5px;
                left: 0;
                background-color: var(--white);
                transition: var(--transition);
            }}
            
            .nav-links a:hover:after {{
                width: 100%;
            }}
            
            .breadcrumb {{
                display: flex;
                gap: 0.5rem;
                padding: 1.5rem 0;
                color: var(--light-text);
            }}
            
            .breadcrumb a {{
                color: var(--primary-color);
                text-decoration: none;
                transition: var(--transition);
            }}
            
            .breadcrumb a:hover {{
                color: var(--secondary-color);
            }}
            
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 20px;
            }}
            
            .product-detail-container {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 3rem;
                margin-bottom: 3rem;
            }}
            
            .product-images {{
                display: flex;
                flex-direction: column;
                gap: 1rem;
            }}
            
            .main-image {{
                width: 100%;
                height: 400px;
                background-color: var(--white);
                border-radius: 8px;
                overflow: hidden;
                box-shadow: var(--shadow);
            }}
            
            .main-image img {{
                width: 100%;
                height: 100%;
                object-fit: contain;
                display: block;
            }}
            
            .thumbnails {{
                display: flex;
                gap: 1rem;
            }}
            
            .thumbnail {{
                width: 80px;
                height: 80px;
                background-color: var(--white);
                border-radius: 8px;
                overflow: hidden;
                cursor: pointer;
                transition: var(--transition);
                opacity: 0.7;
                box-shadow: var(--shadow);
            }}
            
            .thumbnail img {{
                width: 100%;
                height: 100%;
                object-fit: cover;
                display: block;
            }}
            
            .thumbnail.active, .thumbnail:hover {{
                opacity: 1;
                transform: scale(1.05);
            }}
            
            .product-info {{
                background-color: var(--white);
                border-radius: 8px;
                padding: 2rem;
                box-shadow: var(--shadow);
            }}
            
            .product-title {{
                font-size: 2rem;
                margin-bottom: 1rem;
                color: var(--text-color);
            }}
            
            .product-rating {{
                display: flex;
                align-items: center;
                margin-bottom: 1.5rem;
            }}
            
            .stars {{
                color: #ffc107;
                margin-right: 0.75rem;
            }}
            
            .review-count {{
                color: var(--primary-color);
                font-weight: 500;
                cursor: pointer;
                transition: var(--transition);
            }}
            
            .review-count:hover {{
                color: var(--secondary-color);
                text-decoration: underline;
            }}
            
            .price-stock {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 1.5rem;
                padding-bottom: 1.5rem;
                border-bottom: 1px solid var(--gray-200);
            }}
            
            .price {{
                font-size: 2rem;
                font-weight: 700;
                color: var(--accent-color);
            }}
            
            .stock {{
                background-color: #28a745;
                color: var(--white);
                padding: 5px 15px;
                border-radius: 50px;
                font-size: 0.9rem;
                font-weight: 500;
            }}
            
            .stock.low {{
                background-color: #ffc107;
            }}
            
            .stock.out {{
                background-color: #dc3545;
            }}
            
            .product-features {{
                margin: 1.5rem 0;
            }}
            
            .features-title {{
                font-size: 1.3rem;
                margin-bottom: 1rem;
                color: var(--text-color);
            }}
            
            .features-list {{
                list-style: none;
            }}
            
            .features-list li {{
                margin-bottom: 0.75rem;
                font-size: 1rem;
                color: var(--light-text);
            }}
            
            .quantity {{
                display: flex;
                align-items: center;
                gap: 1rem;
                margin-bottom: 1.5rem;
            }}
            
            .quantity-label {{
                font-weight: 500;
            }}
            
            .quantity-selector {{
                display: flex;
                align-items: center;
                border: 1px solid var(--gray-300);
                border-radius: 4px;
                overflow: hidden;
            }}
            
            .quantity-btn {{
                width: 40px;
                height: 40px;
                background-color: var(--gray-100);
                border: none;
                font-size: 1.2rem;
                cursor: pointer;
                transition: var(--transition);
            }}
            
            .quantity-btn:hover {{
                background-color: var(--gray-300);
            }}
            
            .quantity-input {{
                width: 60px;
                height: 40px;
                border: none;
                border-left: 1px solid var(--gray-300);
                border-right: 1px solid var(--gray-300);
                text-align: center;
                font-family: 'Poppins', sans-serif;
                font-size: 1rem;
            }}
            
            .btn-group {{
                display: flex;
                gap: 1rem;
                margin-top: 2rem;
            }}
            
            .btn {{
                flex: 1;
                padding: 1rem 1.5rem;
                border: none;
                border-radius: 4px;
                font-family: 'Poppins', sans-serif;
                font-weight: 600;
                font-size: 1rem;
                cursor: pointer;
                transition: var(--transition);
                text-align: center;
                text-decoration: none;
            }}
            
            .btn-primary {{
                background-color: var(--primary-color);
                color: var(--white);
            }}
            
            .btn-primary:hover {{
                background-color: var(--secondary-color);
            }}
            
            .btn-outline {{
                background-color: transparent;
                border: 2px solid var(--primary-color);
                color: var(--primary-color);
            }}
            
            .btn-outline:hover {{
                background-color: var(--primary-color);
                color: var(--white);
            }}
            
            .description-section {{
                background-color: var(--white);
                border-radius: 8px;
                padding: 2rem;
                margin-bottom: 3rem;
                box-shadow: var(--shadow);
            }}
            
            .section-title {{
                font-size: 1.5rem;
                margin-bottom: 1.5rem;
                color: var(--text-color);
                position: relative;
                padding-bottom: 0.75rem;
            }}
            
            .section-title:after {{
                content: '';
                position: absolute;
                width: 50px;
                height: 3px;
                background-color: var(--accent-color);
                bottom: 0;
                left: 0;
            }}
            
            .description-content {{
                color: var(--light-text);
                line-height: 1.8;
            }}
            
            .related-products {{
                margin-bottom: 5rem;
            }}
            
            .related-products .section-title {{
                text-align: center;
                margin-bottom: 2.5rem;
            }}
            
            .related-products .section-title:after {{
                left: 50%;
                transform: translateX(-50%);
            }}
            
            .products-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
                gap: 2rem;
            }}
            
            .related-product-card {{
                background-color: var(--white);
                border-radius: 8px;
                overflow: hidden;
                box-shadow: var(--shadow);
                transition: var(--transition);
            }}
            
            .related-product-card:hover {{
                transform: translateY(-10px);
                box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
            }}
            
            .related-product-image {{
                height: 150px;
                overflow: hidden;
            }}
            
            .related-product-image img {{
                width: 100%;
                height: 100%;
                object-fit: cover;
                transition: var(--transition);
            }}
            
            .related-product-card:hover .related-product-image img {{
                transform: scale(1.1);
            }}
            
            .related-product-info {{
                padding: 1.5rem;
            }}
            
            .related-product-info h3 {{
                font-size: 1.1rem;
                margin-bottom: 0.5rem;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
            }}
            
            .related-product-price {{
                font-weight: 700;
                color: var(--accent-color);
            }}
            
            footer {{
                background-color: #222;
                color: var(--white);
                padding: 3rem 0;
            }}
            
            .footer-content {{
                max-width: 1200px;
                margin: 0 auto;
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 2rem;
                padding: 0 20px;
            }}
            
            .footer-column h3 {{
                font-size: 1.5rem;
                margin-bottom: 1.5rem;
                position: relative;
                padding-bottom: 10px;
            }}
            
            .footer-column h3:after {{
                content: '';
                position: absolute;
                width: 50px;
                height: 2px;
                background-color: var(--accent-color);
                bottom: 0;
                left: 0;
            }}
            
            .footer-column p, .footer-column a {{
                color: #aaa;
                margin-bottom: 10px;
                display: block;
                text-decoration: none;
                transition: var(--transition);
            }}
            
            .footer-column a:hover {{
                color: var(--white);
                padding-left: 5px;
            }}
            
            .copyright {{
                text-align: center;
                padding-top: 2rem;
                margin-top: 2rem;
                border-top: 1px solid #444;
                color: #aaa;
            }}
            
            /* Responsive styles */
            @media (max-width: 992px) {{
                .product-detail-container {{
                    grid-template-columns: 1fr;
                    gap: 2rem;
                }}
            }}
            
            @media (max-width: 768px) {{
                .main-image {{
                    height: 300px;
                }}
                
                .btn-group {{
                    flex-direction: column;
                }}
                
                .product-title {{
                    font-size: 1.8rem;
                }}
                
                .price {{
                    font-size: 1.8rem;
                }}
            }}
        </style>
    </head>
    <body>
        <header>
            <div class="navbar">
                <a href="/" class="logo">TechVision</a>
                <div class="nav-links">
                    <a href="/">Home</a>
                    <a href="/produk/">Produk</a>
                    <a href="/tentang/">Tentang</a>
                    <a href="/kontak/">Kontak</a>
                </div>
            </div>
        </header>
        
        <div class="container">
            <div class="breadcrumb">
                <a href="/">Home</a> &gt;
                <a href="/produk/">Produk</a> &gt;
                <span>{produk['nama']}</span>
            </div>
            
            <div class="product-detail-container">
                <div class="product-images">
                    <div class="main-image">
                        <img src="{product_images.get(produk['id'], 'https://via.placeholder.com/800x600/4361ee/ffffff?text=Product')}" alt="{produk['nama']}">
                    </div>
                    <div class="thumbnails">
                        {thumbnails_html}
                    </div>
                </div>
                
                <div class="product-info">
                    <h1 class="product-title">{produk['nama']}</h1>
                    
                    <div class="product-rating">
                        <div class="stars">★★★★★</div>
                        <div class="review-count">120 Ulasan</div>
                    </div>
                    
                    <div class="price-stock">
                        <div class="price">Rp {produk['harga']:,}</div>
                        <div class="stock {'low' if produk['stok'] < 10 else 'out' if produk['stok'] == 0 else ''}">
                            {'Stok Terbatas' if produk['stok'] < 10 else 'Stok Habis' if produk['stok'] == 0 else 'Tersedia'}
                        </div>
                    </div>
                    
                    <div class="product-features">
                        <h3 class="features-title">Fitur Utama</h3>
                        <ul class="features-list">
                            {features_list}
                        </ul>
                    </div>
                    
                    <div class="quantity">
                        <div class="quantity-label">Jumlah:</div>
                        <div class="quantity-selector">
                            <button class="quantity-btn">-</button>
                            <input type="text" class="quantity-input" value="1">
                            <button class="quantity-btn">+</button>
                        </div>
                    </div>
                    
                    <div class="btn-group">
                        <a href="#" class="btn btn-primary">Tambah ke Keranjang</a>
                        <a href="#" class="btn btn-outline">Tambah ke Wishlist</a>
                    </div>
                </div>
            </div>
            
            <div class="description-section">
                <h2 class="section-title">Deskripsi Produk</h2>
                <div class="description-content">
                    <p>{produk['deskripsi']}</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris volutpat, quam vel accumsan vestibulum, nunc enim semper mi, nec ullamcorper urna sapien a ligula. Donec euismod, nulla eget accumsan lacinia, nisl nisi commodo libero, in vestibulum ipsum velit ac libero.</p>
                    <p>Suspendisse potenti. Integer vel euismod metus, vel interdum odio. Curabitur volutpat lorem at nunc varius, in pretium sapien tempor. Sed interdum, eros ut placerat fermentum, est lacus aliquam felis, non fermentum nisl ligula eu eros.</p>
                </div>
            </div>
            
            <div class="related-products">
                <h2 class="section-title">Produk Terkait</h2>
                <div class="products-grid">
                    <!-- Related product 1 -->
                    <div class="related-product-card">
                        <div class="related-product-image">
                            <img src="https://via.placeholder.com/250x150/4361ee/ffffff?text=Related1" alt="Related Product 1">
                        </div>
                        <div class="related-product-info">
                            <h3>Produk Terkait 1</h3>
                            <div class="related-product-price">Rp 2,500,000</div>
                        </div>
                    </div>
                    
                    <!-- Related product 2 -->
                    <div class="related-product-card">
                        <div class="related-product-image">
                            <img src="https://via.placeholder.com/250x150/3a0ca3/ffffff?text=Related2" alt="Related Product 2">
                        </div>
                        <div class="related-product-info">
                            <h3>Produk Terkait 2</h3>
                            <div class="related-product-price">Rp 1,800,000</div>
                        </div>
                    </div>
                    
                    <!-- Related product 3 -->
                    <div class="related-product-card">
                        <div class="related-product-image">
                            <img src="https://via.placeholder.com/250x150/4895ef/ffffff?text=Related3" alt="Related Product 3">
                        </div>
                        <div class="related-product-info">
                            <h3>Produk Terkait 3</h3>
                            <div class="related-product-price">Rp 3,200,000</div>
                        </div>
                    </div>
                    
                    <!-- Related product 4 -->
                    <div class="related-product-card">
                        <div class="related-product-image">
                            <img src="https://via.placeholder.com/250x150/4cc9f0/ffffff?text=Related4" alt="Related Product 4">
                        </div>
                        <div class="related-product-info">
                            <h3>Produk Terkait 4</h3>
                            <div class="related-product-price">Rp 1,500,000</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <footer>
            <div class="footer-content">
                <div class="footer-column">
                    <h3>TechVision</h3>
                    <p>Menyediakan produk elektronik premium dengan teknologi terkini untuk mengoptimalkan gaya hidup digital Anda.</p>
                </div>
                
                <div class="footer-column">
                    <h3>Link Cepat</h3>
                    <a href="/">Home</a>
                    <a href="/produk/">Produk</a>
                    <a href="/tentang/">Tentang Kami</a>
                    <a href="/kontak/">Kontak</a>
                </div>
                
                <div class="footer-column">
                    <h3>Kontak</h3>
                    <p>Jl. Contoh No. 123, Jakarta</p>
                    <p>info@techvision.com</p>
                    <p>(021) 123-4567</p>
                </div>
                
                <div class="footer-column">
                    <h3>Jam Operasional</h3>
                    <p>Senin - Jumat: 08:00 - 17:00</p>
                    <p>Sabtu: 09:00 - 15:00</p>
                    <p>Minggu: Tutup</p>
                </div>
            </div>
            
            <div class="copyright">
                <p>&copy; 2025 TechVision. All Rights Reserved.</p>
            </div>
        </footer>
    </body>
    </html>
    """
    return HttpResponse(html_content)

def tentang_kami(request):
    """View untuk halaman tentang kami (/tentang/)"""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Tentang Kami - TechVision</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
        <style>
            :root {
                --primary-color: #4361ee;
                --secondary-color: #3f37c9;
                --accent-color: #f72585;
                --bg-color: #f8f9fa;
                --text-color: #333;
                --light-text: #6c757d;
                --white: #ffffff;
                --shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                --transition: all 0.3s ease;
                --gray-100: #f8f9fa;
                --gray-200: #e9ecef;
                --gray-300: #dee2e6;
            }
            
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Poppins', sans-serif;
                line-height: 1.6;
                color: var(--text-color);
                background-color: var(--bg-color);
                overflow-x: hidden;
            }
            
            header {
                background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
                padding: 1.5rem 0;
                position: sticky;
                top: 0;
                z-index: 100;
                box-shadow: var(--shadow);
            }
            
            .navbar {
                display: flex;
                justify-content: space-between;
                align-items: center;
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 20px;
            }
            
            .logo {
                font-size: 1.8rem;
                font-weight: 700;
                color: var(--white);
                text-decoration: none;
            }
            
            .nav-links {
                display: flex;
                gap: 2rem;
            }
            
            .nav-links a {
                color: var(--white);
                text-decoration: none;
                font-weight: 500;
                font-size: 1.1rem;
                transition: var(--transition);
                position: relative;
            }
            
            .nav-links a:after {
                content: '';
                position: absolute;
                width: 0;
                height: 2px;
                bottom: -5px;
                left: 0;
                background-color: var(--white);
                transition: var(--transition);
            }
            
            .nav-links a:hover:after {
                width: 100%;
            }
            
            .page-header {
                background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
                padding: 5rem 0;
                color: var(--white);
                text-align: center;
                position: relative;
                overflow: hidden;
            }
            
            .page-header:before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: url('https://images.unsplash.com/photo-1531297484001-80022131f5a1?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80') no-repeat center center/cover;
                opacity: 0.2;
            }
            
            .page-header h1 {
                font-size: 3rem;
                margin-bottom: 1rem;
                position: relative;
                z-index: 2;
            }
            
            .page-header p {
                font-size: 1.2rem;
                max-width: 800px;
                margin: 0 auto;
                position: relative;
                z-index: 2;
            }
            
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 5rem 20px;
            }
            
            .about-section {
                margin-bottom: 5rem;
            }
            
            .section-title {
                font-size: 2.5rem;
                margin-bottom: 2rem;
                text-align: center;
                position: relative;
                padding-bottom: 1rem;
            }
            
            .section-title:after {
                content: '';
                position: absolute;
                width: 100px;
                height: 3px;
                background-color: var(--accent-color);
                bottom: 0;
                left: 50%;
                transform: translateX(-50%);
            }
            
            .vision-mission {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 2rem;
                margin-top: 3rem;
            }
            
            .vision-card, .mission-card {
                background-color: var(--white);
                border-radius: 8px;
                padding: 2rem;
                box-shadow: var(--shadow);
                transition: var(--transition);
                text-align: center;
            }
            
            .vision-card:hover, .mission-card:hover {
                transform: translateY(-10px);
                box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
            }
            
            .card-icon {
                font-size: 3rem;
                color: var(--primary-color);
                margin-bottom: 1.5rem;
            }
            
            .card-title {
                font-size: 1.8rem;
                margin-bottom: 1rem;
                color: var(--secondary-color);
            }
            
            .mission-list {
                text-align: left;
                padding-left: 1.5rem;
                margin-top: 1.5rem;
            }
            
            .mission-list li {
                margin-bottom: 1rem;
                position: relative;
            }
            
            .mission-list li:before {
                content: '✓';
                position: absolute;
                left: -1.5rem;
                color: var(--accent-color);
                font-weight: bold;
            }
            
            .timeline-section {
                padding: 5rem 0;
                background-color: var(--gray-100);
                position: relative;
            }
            
            .timeline {
                position: relative;
                max-width: 800px;
                margin: 3rem auto 0;
            }
            
            .timeline:before {
                content: '';
                position: absolute;
                height: 100%;
                width: 4px;
                background-color: var(--primary-color);
                left: 50%;
                transform: translateX(-50%);
            }
            
            .timeline-item {
                padding: 1.5rem 0;
                position: relative;
                width: 50%;
            }
            
            .timeline-item:nth-child(odd) {
                left: 0;
                padding-right: 40px;
                text-align: right;
            }
            
            .timeline-item:nth-child(even) {
                left: 50%;
                padding-left: 40px;
            }
            
            .timeline-item:after {
                content: '';
                position: absolute;
                width: 20px;
                height: 20px;
                background-color: var(--white);
                border: 4px solid var(--accent-color);
                border-radius: 50%;
                top: calc(1.5rem + 10px);
            }
            
            .timeline-item:nth-child(odd):after {
                right: -12px;
            }
            
            .timeline-item:nth-child(even):after {
                left: -12px;
            }
            
            .timeline-content {
                background-color: var(--white);
                border-radius: 8px;
                padding: 1.5rem;
                box-shadow: var(--shadow);
            }
            
            .timeline-year {
                font-size: 1.5rem;
                font-weight: 700;
                color: var(--accent-color);
                margin-bottom: 0.5rem;
            }
            
            .team-section {
                padding: 5rem 0;
            }
            
            .team-grid {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
                gap: 2rem;
                margin-top: 3rem;
            }
            
            .team-member {
                background-color: var(--white);
                border-radius: 8px;
                overflow: hidden;
                box-shadow: var(--shadow);
                transition: var(--transition);
            }
            
            .team-member:hover {
                transform: translateY(-10px);
                box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
            }
            
            .member-image {
                height: 250px;
                background-color: var(--gray-300);
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 5rem;
                color: var(--gray-500);
            }
            
            .member-info {
                padding: 1.5rem;
                text-align: center;
            }
            
            .member-name {
                font-size: 1.5rem;
                margin-bottom: 0.5rem;
                color: var(--text-color);
            }
            
            .member-role {
                color: var(--accent-color);
                font-weight: 500;
                margin-bottom: 1rem;
            }
            
            .social-links {
                display: flex;
                justify-content: center;
                gap: 1rem;
                margin-top: 1rem;
            }
            
            .social-link {
                width: 35px;
                height: 35px;
                border-radius: 50%;
                background-color: var(--primary-color);
                color: var(--white);
                display: flex;
                align-items: center;
                justify-content: center;
                text-decoration: none;
                transition: var(--transition);
            }
            
            .social-link:hover {
                background-color: var(--secondary-color);
                transform: scale(1.1);
            }
            
            .cta-section {
                background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
                padding: 5rem 0;
                text-align: center;
                color: var(--white);
            }
            
            .cta-content {
                max-width: 800px;
                margin: 0 auto;
            }
            
            .cta-section h2 {
                font-size: 2.5rem;
                margin-bottom: 1.5rem;
            }
            
            .cta-section p {
                font-size: 1.2rem;
                margin-bottom: 2rem;
            }
            
            .cta-btn {
                display: inline-block;
                background-color: var(--white);
                color: var(--primary-color);
                padding: 1rem 2rem;
                border-radius: 50px;
                text-decoration: none;
                font-weight: 600;
                transition: var(--transition);
                box-shadow: var(--shadow);
            }
            
            .cta-btn:hover {
                transform: translateY(-3px);
                box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
            }
            
            footer {
                background-color: #222;
                color: var(--white);
                padding: 3rem 0;
            }
            
            .footer-content {
                max-width: 1200px;
                margin: 0 auto;
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 2rem;
                padding: 0 20px;
            }
            
            .footer-column h3 {
                font-size: 1.5rem;
                margin-bottom: 1.5rem;
                position: relative;
                padding-bottom: 10px;
            }
            
            .footer-column h3:after {
                content: '';
                position: absolute;
                width: 50px;
                height: 2px;
                background-color: var(--accent-color);
                bottom: 0;
                left: 0;
            }
            
            .footer-column p, .footer-column a {
                color: #aaa;
                margin-bottom: 10px;
                display: block;
                text-decoration: none;
                transition: var(--transition);
            }
            
            .footer-column a:hover {
                color: var(--white);
                padding-left: 5px;
            }
            
            .copyright {
                text-align: center;
                padding-top: 2rem;
                margin-top: 2rem;
                border-top: 1px solid #444;
                color: #aaa;
            }
            
            /* Responsive styles */
            @media (max-width: 992px) {
                .page-header h1 {
                    font-size: 2.5rem;
                }
                
                .section-title {
                    font-size: 2rem;
                }
            }
            
            @media (max-width: 768px) {
                .timeline:before {
                    left: 40px;
                }
                
                .timeline-item {
                    width: 100%;
                    padding-left: 70px;
                    padding-right: 0;
                    text-align: left;
                }
                
                .timeline-item:nth-child(odd) {
                    left: 0;
                    padding-right: 0;
                    text-align: left;
                }
                
                .timeline-item:nth-child(even) {
                    left: 0;
                }
                
                .timeline-item:after {
                    left: 28px;
                }
                
                .timeline-item:nth-child(odd):after {
                    left: 28px;
                    right: auto;
                }
            }
        </style>
    </head>
    <body>
        <header>
            <div class="navbar">
                <a href="/" class="logo">TechVision</a>
                <div class="nav-links">
                    <a href="/">Home</a>
                    <a href="/produk/">Produk</a>
                    <a href="/tentang/">Tentang</a>
                    <a href="/kontak/">Kontak</a>
                </div>
            </div>
        </header>
        
        <div class="page-header">
            <div class="container">
                <h1>Tentang TechVision</h1>
                <p>Menghubungkan Inovasi & Teknologi untuk Masa Depan yang Lebih Baik</p>
            </div>
        </div>
        
        <div class="container">
            <div class="about-section">
                <h2 class="section-title">Visi & Misi Kami</h2>
                <div class="vision-mission">
                    <div class="vision-card">
                        <div class="card-icon">👁️</div>
                        <h3 class="card-title">Visi Kami</h3>
                        <p>Menjadi penyedia produk elektronik terpercaya dengan kualitas terbaik dan harga yang kompetitif di Indonesia, serta menjadi mitra teknologi pilihan bagi individu dan bisnis.</p>
                    </div>
                    
                    <div class="mission-card">
                        <div class="card-icon">🎯</div>
                        <h3 class="card-title">Misi Kami</h3>
                        <ul class="mission-list">
                            <li>Menyediakan produk elektronik berkualitas tinggi dengan pelayanan yang prima untuk kepuasan pelanggan.</li>
                            <li>Membangun hubungan jangka panjang dengan pelanggan melalui layanan purna jual yang memuaskan.</li>
                            <li>Berkontribusi dalam perkembangan teknologi di Indonesia dengan edukasi dan inovasi.</li>
                            <li>Menerapkan praktik bisnis yang berkelanjutan dan ramah lingkungan.</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="timeline-section">
            <div class="container">
                <h2 class="section-title">Sejarah Perusahaan</h2>
                <div class="timeline">
                    <div class="timeline-item">
                        <div class="timeline-content">
                            <div class="timeline-year">2010</div>
                            <h3>Awal Mula</h3>
                            <p>TechVision didirikan dengan fokus pada penjualan produk komputer dan layanan IT untuk bisnis kecil dan menengah.</p>
                        </div>
                    </div>
                    
                    <div class="timeline-item">
                        <div class="timeline-content">
                            <div class="timeline-year">2015</div>
                            <h3>Ekspansi Produk</h3>
                            <p>Memperluas jangkauan produk ke perangkat elektronik konsumen seperti smartphone, tablet, dan aksesori.</p>
                        </div>
                    </div>
                    
                    <div class="timeline-item">
                        <div class="timeline-content">
                            <div class="timeline-year">2018</div>
                            <h3>Era Digital</h3>
                            <p>Meluncurkan platform e-commerce untuk menjangkau pasar nasional dan meningkatkan pelayanan kepada pelanggan.</p>
                        </div>
                    </div>
                    
                    <div class="timeline-item">
                        <div class="timeline-content">
                            <div class="timeline-year">2020</div>
                            <h3>Inovasi Layanan</h3>
                            <p>Menambahkan layanan konsultasi teknologi dan dukungan teknis 24/7 untuk meningkatkan pengalaman pelanggan.</p>
                        </div>
                    </div>
                    
                    <div class="timeline-item">
                        <div class="timeline-content">
                            <div class="timeline-year">2023</div>
                            <h3>Ekspansi Nasional</h3>
                            <p>Membuka cabang fisik di beberapa kota besar di Indonesia dan menjadi distributor resmi untuk beberapa merek teknologi terkemuka.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="container">
            <div class="team-section">
                <h2 class="section-title">Tim Kami</h2>
                <p style="text-align: center; margin-bottom: 3rem;">Kami memiliki tim profesional berdedikasi yang siap memberikan layanan terbaik untuk Anda.</p>
                
                <div class="team-grid">
                    <div class="team-member">
                        <div class="member-image">👨‍💼</div>
                        <div class="member-info">
                            <h3 class="member-name">John Doe</h3>
                            <p class="member-role">CEO & Founder</p>
                            <p>Berpengalaman lebih dari 15 tahun di industri teknologi, dengan visi untuk membuat teknologi terjangkau bagi semua orang.</p>
                            <div class="social-links">
                                <a href="#" class="social-link">f</a>
                                <a href="#" class="social-link">in</a>
                                <a href="#" class="social-link">tw</a>
                            </div>
                        </div>
                    </div>
                    
                    <div class="team-member">
                        <div class="member-image">👩‍💼</div>
                        <div class="member-info">
                            <h3 class="member-name">Jane Smith</h3>
                            <p class="member-role">CTO</p>
                            <p>Ahli di bidang hardware dan software dengan latar belakang pendidikan dari MIT dan pengalaman di perusahaan teknologi global.</p>
                            <div class="social-links">
                                <a href="#" class="social-link">f</a>
                                <a href="#" class="social-link">in</a>
                                <a href="#" class="social-link">tw</a>
                            </div>
                        </div>
                    </div>
                    
                    <div class="team-member">
                        <div class="member-image">👨‍💼</div>
                        <div class="member-info">
                            <h3 class="member-name">Michael Johnson</h3>
                            <p class="member-role">Marketing Director</p>
                            <p>Spesialis marketing digital dengan fokus pada pengembangan strategi pemasaran berbasis data dan analitik.</p>
                            <div class="social-links">
                                <a href="#" class="social-link">f</a>
                                <a href="#" class="social-link">in</a>
                                <a href="#" class="social-link">tw</a>
                            </div>
                        </div>
                    </div>
                    
                    <div class="team-member">
                        <div class="member-image">👩‍💼</div>
                        <div class="member-info">
                            <h3 class="member-name">Sarah Williams</h3>
                            <p class="member-role">Customer Service Head</p>
                            <p>Memimpin tim layanan pelanggan dengan fokus pada penyelesaian masalah yang cepat dan pengalaman pelanggan yang luar biasa.</p>
                            <div class="social-links">
                                <a href="#" class="social-link">f</a>
                                <a href="#" class="social-link">in</a>
                                <a href="#" class="social-link">tw</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="cta-section">
            <div class="cta-content">
                <h2>Bergabunglah dengan Komunitas TechVision</h2>
                <p>Dapatkan informasi terbaru tentang produk, promosi, dan tips teknologi langsung di inbox Anda.</p>
                <a href="/kontak/" class="cta-btn">Hubungi Kami Sekarang</a>
            </div>
        </div>
        
        <footer>
            <div class="footer-content">
                <div class="footer-column">
                    <h3>TechVision</h3>
                    <p>Menyediakan produk elektronik premium dengan teknologi terkini untuk mengoptimalkan gaya hidup digital Anda.</p>
                </div>
                
                <div class="footer-column">
                    <h3>Link Cepat</h3>
                    <a href="/">Home</a>
                    <a href="/produk/">Produk</a>
                    <a href="/tentang/">Tentang Kami</a>
                    <a href="/kontak/">Kontak</a>
                </div>
                
                <div class="footer-column">
                    <h3>Kontak</h3>
                    <p>Jl. Contoh No. 123, Jakarta</p>
                    <p>info@techvision.com</p>
                    <p>(021) 123-4567</p>
                </div>
                
                <div class="footer-column">
                    <h3>Jam Operasional</h3>
                    <p>Senin - Jumat: 08:00 - 17:00</p>
                    <p>Sabtu: 09:00 - 15:00</p>
                    <p>Minggu: Tutup</p>
                </div>
            </div>
            
            <div class="copyright">
                <p>&copy; 2025 TechVision. All Rights Reserved.</p>
            </div>
        </footer>
    </body>
    </html>
    """
    return HttpResponse(html_content)

def kontak(request):
    """View untuk halaman kontak (/kontak/)"""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Kontak Kami - TechVision</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
        <style>
            :root {
                --primary-color: #4361ee;
                --secondary-color: #3f37c9;
                --accent-color: #f72585;
                --bg-color: #f8f9fa;
                --text-color: #333;
                --light-text: #6c757d;
                --white: #ffffff;
                --shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                --transition: all 0.3s ease;
                --gray-100: #f8f9fa;
                --gray-200: #e9ecef;
                --gray-300: #dee2e6;
                --gray-400: #ced4da;
                --gray-500: #adb5bd;
            }
            
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Poppins', sans-serif;
                line-height: 1.6;
                color: var(--text-color);
                background-color: var(--bg-color);
                overflow-x: hidden;
            }
            
            header {
                background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
                padding: 1.5rem 0;
                position: sticky;
                top: 0;
                z-index: 100;
                box-shadow: var(--shadow);
            }
            
            .navbar {
                display: flex;
                justify-content: space-between;
                align-items: center;
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 20px;
            }
            
            .logo {
                font-size: 1.8rem;
                font-weight: 700;
                color: var(--white);
                text-decoration: none;
            }
            
            .nav-links {
                display: flex;
                gap: 2rem;
            }
            
            .nav-links a {
                color: var(--white);
                text-decoration: none;
                font-weight: 500;
                font-size: 1.1rem;
                transition: var(--transition);
                position: relative;
            }
            
            .nav-links a:after {
                content: '';
                position: absolute;
                width: 0;
                height: 2px;
                bottom: -5px;
                left: 0;
                background-color: var(--white);
                transition: var(--transition);
            }
            
            .nav-links a:hover:after {
                width: 100%;
            }
            
            .page-header {
                background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
                padding: 5rem 0;
                color: var(--white);
                text-align: center;
                position: relative;
                overflow: hidden;
            }
            
            .page-header:before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: url('https://images.unsplash.com/photo-1516321318423-f06f85e504b3?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80') no-repeat center center/cover;
                opacity: 0.2;
            }
            
            .page-header h1 {
                font-size: 3rem;
                margin-bottom: 1rem;
                position: relative;
                z-index: 2;
            }
            
            .page-header p {
                font-size: 1.2rem;
                max-width: 800px;
                margin: 0 auto;
                position: relative;
                z-index: 2;
            }
            
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 5rem 20px;
            }
            
            .contact-container {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 3rem;
                margin-bottom: 5rem;
            }
            
            .contact-info {
                padding: 2rem;
                background-color: var(--white);
                border-radius: 8px;
                box-shadow: var(--shadow);
            }
            
            .info-title {
                font-size: 1.8rem;
                margin-bottom: 2rem;
                color: var(--text-color);
                position: relative;
                padding-bottom: 1rem;
            }
            
            .info-title:after {
                content: '';
                position: absolute;
                width: 50px;
                height: 3px;
                background-color: var(--accent-color);
                bottom: 0;
                left: 0;
            }
            
            .info-item {
                display: flex;
                margin-bottom: 1.5rem;
            }
            
            .info-icon {
                background-color: rgba(67, 97, 238, 0.1);
                width: 50px;
                height: 50px;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                margin-right: 1rem;
                font-size: 1.5rem;
                color: var(--primary-color);
            }
            
            .info-text h3 {
                font-size: 1.2rem;
                margin-bottom: 0.5rem;
                color: var(--text-color);
            }
            
            .info-text p {
                color: var(--light-text);
                line-height: 1.5;
            }
            
            .social-media {
                margin-top: 3rem;
            }
            
            .social-title {
                font-size: 1.5rem;
                margin-bottom: 1.5rem;
                color: var(--text-color);
            }
            
            .social-links {
                display: flex;
                gap: 1rem;
            }
            
            .social-link {
                width: 40px;
                height: 40px;
                border-radius: 50%;
                background-color: var(--primary-color);
                color: var(--white);
                display: flex;
                align-items: center;
                justify-content: center;
                text-decoration: none;
                transition: var(--transition);
                font-size: 1.2rem;
            }
            
            .social-link:hover {
                background-color: var(--secondary-color);
                transform: scale(1.1);
            }
            
            .contact-form {
                padding: 2rem;
                background-color: var(--white);
                border-radius: 8px;
                box-shadow: var(--shadow);
            }
            
            .form-title {
                font-size: 1.8rem;
                margin-bottom: 2rem;
                color: var(--text-color);
                position: relative;
                padding-bottom: 1rem;
            }
            
            .form-title:after {
                content: '';
                position: absolute;
                width: 50px;
                height: 3px;
                background-color: var(--accent-color);
                bottom: 0;
                left: 0;
            }
            
            .form-group {
                margin-bottom: 1.5rem;
            }
            
            .form-label {
                display: block;
                margin-bottom: 0.5rem;
                font-weight: 500;
                color: var(--text-color);
            }
            
            .form-control {
                width: 100%;
                padding: 12px 15px;
                border: 1px solid var(--gray-300);
                border-radius: 4px;
                font-family: 'Poppins', sans-serif;
                font-size: 1rem;
                transition: var(--transition);
            }
            
            .form-control:focus {
                outline: none;
                border-color: var(--primary-color);
                box-shadow: 0 0 0 3px rgba(67, 97, 238, 0.1);
            }
            
            textarea.form-control {
                min-height: 150px;
                resize: vertical;
            }
            
            .form-button {
                background-color: var(--primary-color);
                color: var(--white);
                border: none;
                padding: 12px 25px;
                border-radius: 4px;
                font-family: 'Poppins', sans-serif;
                font-size: 1rem;
                font-weight: 600;
                cursor: pointer;
                transition: var(--transition);
            }
            
            .form-button:hover {
                background-color: var(--secondary-color);
                transform: translateY(-3px);
                box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
            }
            
            .map-section {
                background-color: var(--white);
                border-radius: 8px;
                padding: 2rem;
                box-shadow: var(--shadow);
                margin-bottom: 3rem;
            }
            
            .map-title {
                font-size: 1.8rem;
                margin-bottom: 2rem;
                color: var(--text-color);
                position: relative;
                padding-bottom: 1rem;
                text-align: center;
            }
            
            .map-title:after {
                content: '';
                position: absolute;
                width: 50px;
                height: 3px;
                background-color: var(--accent-color);
                bottom: 0;
                left: 50%;
                transform: translateX(-50%);
            }
            
            .map-container {
                height: 400px;
                background-color: var(--gray-200);
                border-radius: 4px;
                display: flex;
                align-items: center;
                justify-content: center;
                color: var(--gray-500);
                font-size: 1.5rem;
            }
            
            .faq-section {
                margin-bottom: 5rem;
            }
            
            .faq-title {
                font-size: 2rem;
                margin-bottom: 2rem;
                color: var(--text-color);
                text-align: center;
                position: relative;
                padding-bottom: 1rem;
            }
            
            .faq-title:after {
                content: '';
                position: absolute;
                width: 50px;
                height: 3px;
                background-color: var(--accent-color);
                bottom: 0;
                left: 50%;
                transform: translateX(-50%);
            }
            
            .faq-container {
                max-width: 800px;
                margin: 0 auto;
            }
            
            .faq-item {
                background-color: var(--white);
                border-radius: 8px;
                margin-bottom: 1rem;
                overflow: hidden;
                box-shadow: var(--shadow);
            }
            
            .faq-question {
                padding: 1.5rem;
                background-color: var(--white);
                font-weight: 600;
                color: var(--text-color);
                cursor: pointer;
                position: relative;
            }
            
            .faq-question:after {
                content: '+';
                position: absolute;
                right: 1.5rem;
                top: 50%;
                transform: translateY(-50%);
                font-size: 1.5rem;
                color: var(--primary-color);
            }
            
            .faq-answer {
                padding: 0 1.5rem 1.5rem;
                color: var(--light-text);
                line-height: 1.8;
            }
            
            footer {
                background-color: #222;
                color: var(--white);
                padding: 3rem 0;
            }
            
            .footer-content {
                max-width: 1200px;
                margin: 0 auto;
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 2rem;
                padding: 0 20px;
            }
            
            .footer-column h3 {
                font-size: 1.5rem;
                margin-bottom: 1.5rem;
                position: relative;
                padding-bottom: 10px;
            }
            
            .footer-column h3:after {
                content: '';
                position: absolute;
                width: 50px;
                height: 2px;
                background-color: var(--accent-color);
                bottom: 0;
                left: 0;
            }
            
            .footer-column p, .footer-column a {
                color: #aaa;
                margin-bottom: 10px;
                display: block;
                text-decoration: none;
                transition: var(--transition);
            }
            
            .footer-column a:hover {
                color: var(--white);
                padding-left: 5px;
            }
            
            .copyright {
                text-align: center;
                padding-top: 2rem;
                margin-top: 2rem;
                border-top: 1px solid #444;
                color: #aaa;
            }
            
            /* Responsive styles */
            @media (max-width: 992px) {
                .contact-container {
                    grid-template-columns: 1fr;
                }
                
                .page-header h1 {
                    font-size: 2.5rem;
                }
            }
            
            @media (max-width: 768px) {
                .page-header {
                    padding: 3rem 0;
                }
                
                .page-header h1 {
                    font-size: 2rem;
                }
                
                .info-title, .form-title, .map-title, .faq-title {
                    font-size: 1.5rem;
                }
            }
        </style>
    </head>
    <body>
        <header>
            <div class="navbar">
                <a href="/" class="logo">TechVision</a>
                <div class="nav-links">
                    <a href="/">Home</a>
                    <a href="/produk/">Produk</a>
                    <a href="/tentang/">Tentang</a>
                    <a href="/kontak/">Kontak</a>
                </div>
            </div>
        </header>
        
        <div class="page-header">
            <div class="container">
                <h1>Hubungi Kami</h1>
                <p>Kami siap membantu Anda dengan pertanyaan, saran, atau kebutuhan apa pun</p>
            </div>
        </div>
        
        <div class="container">
            <div class="contact-container">
                <div class="contact-info">
                    <h2 class="info-title">Informasi Kontak</h2>
                    
                    <div class="info-item">
                        <div class="info-icon">📍</div>
                        <div class="info-text">
                            <h3>Alamat</h3>
                            <p>Jl. Contoh No. 123, Jakarta Selatan,<br>Indonesia 12345</p>
                        </div>
                    </div>
                    
                    <div class="info-item">
                        <div class="info-icon">📱</div>
                        <div class="info-text">
                            <h3>Telepon</h3>
                            <p>(021) 123-4567</p>
                            <p>0812-3456-7890</p>
                        </div>
                    </div>
                    
                    <div class="info-item">
                        <div class="info-icon">✉️</div>
                        <div class="info-text">
                            <h3>Email</h3>
                            <p>info@techvision.com</p>
                            <p>support@techvision.com</p>
                        </div>
                    </div>
                    
                    <div class="info-item">
                        <div class="info-icon">⏰</div>
                        <div class="info-text">
                            <h3>Jam Operasional</h3>
                            <p>Senin - Jumat: 08:00 - 17:00</p>
                            <p>Sabtu: 09:00 - 15:00</p>
                            <p>Minggu: Tutup</p>
                        </div>
                    </div>
                    
                    <div class="social-media">
                        <h3 class="social-title">Ikuti Kami</h3>
                        <div class="social-links">
                            <a href="#" class="social-link">f</a>
                            <a href="#" class="social-link">in</a>
                            <a href="#" class="social-link">tw</a>
                            <a href="#" class="social-link">ig</a>
                            <a href="#" class="social-link">yt</a>
                        </div>
                    </div>
                </div>
                
                <div class="contact-form">
                    <h2 class="form-title">Kirim Pesan</h2>
                    
                    <form action="#" method="POST">
                        <div class="form-group">
                            <label for="name" class="form-label">Nama Lengkap</label>
                            <input type="text" id="name" name="name" class="form-control" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="email" class="form-label">Email</label>
                            <input type="email" id="email" name="email" class="form-control" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="phone" class="form-label">Telepon</label>
                            <input type="tel" id="phone" name="phone" class="form-control">
                        </div>
                        
                        <div class="form-group">
                            <label for="subject" class="form-label">Subjek</label>
                            <input type="text" id="subject" name="subject" class="form-control" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="message" class="form-label">Pesan</label>
                            <textarea id="message" name="message" class="form-control" required></textarea>
                        </div>
                        
                        <button type="submit" class="form-button">Kirim Pesan</button>
                    </form>
                </div>
            </div>
            
            <div class="map-section">
                <h2 class="map-title">Lokasi Kami</h2>
                <div class="map-container">
                    [Peta Lokasi TechVision]
                </div>
            </div>
            
            <div class="faq-section">
                <h2 class="faq-title">Pertanyaan Umum</h2>
                <div class="faq-container">
                    <div class="faq-item">
                        <div class="faq-question">Bagaimana cara melakukan pemesanan?</div>
                        <div class="faq-answer">
                            <p>Anda dapat melakukan pemesanan melalui website kami dengan memilih produk yang diinginkan, menambahkannya ke keranjang, dan mengikuti proses checkout. Anda juga dapat melakukan pemesanan melalui telepon atau email.</p>
                        </div>
                    </div>
                    
                    <div class="faq-item">
                        <div class="faq-question">Berapa lama waktu pengiriman?</div>
                        <div class="faq-answer">
                            <p>Waktu pengiriman tergantung pada lokasi Anda. Untuk wilayah Jakarta biasanya 1-2 hari kerja, untuk luar Jakarta 3-5 hari kerja, dan untuk daerah terpencil bisa mencapai 5-7 hari kerja.</p>
                        </div>
                    </div>
                    
                    <div class="faq-item">
                        <div class="faq-question">Apakah ada garansi untuk produk yang dibeli?</div>
                        <div class="faq-answer">
                            <p>Ya, semua produk kami dilengkapi dengan garansi resmi dari produsen. Lama garansi bervariasi tergantung jenis produk, mulai dari 12 bulan hingga 36 bulan.</p>
                        </div>
                    </div>
                    
                    <div class="faq-item">
                        <div class="faq-question">Bagaimana jika produk yang saya terima rusak?</div>
                        <div class="faq-answer">
                            <p>Jika Anda menerima produk yang rusak, silakan hubungi tim layanan pelanggan kami dalam waktu 7 hari setelah penerimaan. Kami akan memproses penggantian atau pengembalian dana sesuai dengan kebijakan kami.</p>
                        </div>
                    </div>
                    
                    <div class="faq-item">
                        <div class="faq-question">Apakah ada biaya pengiriman?</div>
                        <div class="faq-answer">
                            <p>Ya, biaya pengiriman tergantung pada berat produk dan lokasi pengiriman. Untuk pembelian dengan nilai tertentu, kami menyediakan pengiriman gratis. Detail lebih lanjut dapat dilihat saat proses checkout.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <footer>
            <div class="footer-content">
                <div class="footer-column">
                    <h3>TechVision</h3>
                    <p>Menyediakan produk elektronik premium dengan teknologi terkini untuk mengoptimalkan gaya hidup digital Anda.</p>
                </div>
                
                <div class="footer-column">
                    <h3>Link Cepat</h3>
                    <a href="/">Home</a>
                    <a href="/produk/">Produk</a>
                    <a href="/tentang/">Tentang Kami</a>
                    <a href="/kontak/">Kontak</a>
                </div>
                
                <div class="footer-column">
                    <h3>Kontak</h3>
                    <p>Jl. Contoh No. 123, Jakarta</p>
                    <p>info@techvision.com</p>
                    <p>(021) 123-4567</p>
                </div>
                
                <div class="footer-column">
                    <h3>Jam Operasional</h3>
                    <p>Senin - Jumat: 08:00 - 17:00</p>
                    <p>Sabtu: 09:00 - 15:00</p>
                    <p>Minggu: Tutup</p>
                </div>
            </div>
            
            <div class="copyright">
                <p>&copy; 2025 TechVision. All Rights Reserved.</p>
            </div>
        </footer>
    </body>
    </html>
    """
    return HttpResponse(html_content)