<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Meta tags for character encoding and viewport -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Info Portal</title>
    
    <!-- Internal CSS for basic styling -->
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }
        
        /* Header Styles */
        header {
            background-color: #2c3e50;
            color: white;
            padding: 1.5rem 0;
            text-align: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        header h1 {
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }
        
        header p {
            font-size: 1rem;
            opacity: 0.9;
        }
        
        /* Navigation Styles */
        nav {
            background-color: #34495e;
            padding: 1rem 0;
        }
        
        nav ul {
            list-style: none;
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
        }
        
        nav ul li {
            margin: 0 1.5rem;
        }
        
        nav ul li a {
            color: white;
            text-decoration: none;
            font-size: 1.1rem;
            padding: 0.5rem 1rem;
            display: block;
            transition: background-color 0.3s;
        }
        
        nav ul li a:hover {
            background-color: #2c3e50;
            border-radius: 4px;
        }
        
        /* Main Content Area */
        main {
            flex: 1;
            padding: 2rem;
            max-width: 1200px;
            margin: 0 auto;
            width: 100%;
        }
        
        /* Footer Styles */
        footer {
            background-color: #2c3e50;
            color: white;
            text-align: center;
            padding: 1.5rem 0;
            margin-top: auto;
        }
        
        footer p {
            margin: 0.5rem 0;
        }
    </style>
</head>
<body>
    <!-- Header Section -->
    <header>
        <h1>Student Info Portal</h1>
        <p>Your gateway to academic information and resources</p>
    </header>
    
    <!-- Navigation Menu -->
    <nav>
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#students">Students</a></li>
            <li><a href="#courses">Courses</a></li>
            <li><a href="#grades">Grades</a></li>
            <li><a href="#about">About</a></li>
        </ul>
    </nav>
    
    <!-- Main Content Area -->
    <main>
        <h2>Welcome Dandu Deekshith</h2>
        <p>This portal provides access to student information, course details, and academic resources.</p>
    </main>
    
    <!-- Footer Section -->
    <footer>
        <p>&copy; 2025 Student Info Portal. All rights reserved.</p>
        <p>Contact: info@studentportal.edu</p>
    </footer>
</body>
</html>
