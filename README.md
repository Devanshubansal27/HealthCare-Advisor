# Health Buddy - AI-Powered Healthcare Advisor 🩺
<img width="1431" alt="banner" src="https://github.com/user-attachments/assets/f47fc3a8-0d76-4c2e-88b5-4ada871ff1b1">

Get personalized health insights and guidance with Health Buddy.
Health Buddy is a Streamlit application powered by Gemini’s AI that provides health advice and BMI calculations. Leveraging advanced AI capabilities, it offers responses to various health questions, helping users make informed wellness decisions.

Features

	• Health Advice: Ask general health questions and get AI-powered advice tailored to your concerns.
	• BMI Calculator: Calculate your Body Mass Index to assess your health status based on weight and height.
	• AI-Powered Insights: Leverages Google’s Gemini model for generating responses, providing personalized, relevant information.

How to Use

	1. Health Advice: Simply type your health-related query into the input box, and Health Buddy will respond with AI-driven insights. After each response, you can provide feedback on its helpfulness and receive alternative responses if needed.
	2. BMI Calculator: Enter your weight and height to get your BMI score and an associated health category (e.g., Underweight, Normal, Overweight, Obesity).

Technical Stack

	• Streamlit: For building the interactive web application.
	• Python-dotenv: For managing environment variables, such as API keys.
	• Google GenerativeAI: Utilizes Gemini AI for generating health-related advice and responses.
	• Pandas: For handling data in the BMI calculator.

Installation

	1. Clone the repository: git clone https://github.com/your-username/Health-Buddy.git
	2. Navigate to the project directory: cd Health-Buddy
	3. Create a virtual environment: python -m venv .venv
	4. Activate the virtual environment:
		• On Windows: .venv\Scripts\activate
		•On macOS/Linux: source .venv/bin/activate
	5. Install the dependencies: pip install -r requirements.txt
	6. Set up your Gemini API key:
		• Create a .env file in the root directory.
	        • Add your API key in this format: GOOGLE-API-KEY=your_gemini_api_key_here
	7. Run the app: streamlit run app.py

Example Usage

	1. For Health Advice: Enter questions like, “How to manage stress?” or “What are the benefits of regular exercise?” in the Health Advice section. You will get AI-driven responses that are tailored for general health and wellness.
	2. For BMI Calculation: In the BMI Calculator section, enter your weight (in kg) and height (in cm) to calculate your Body Mass Index. The app will also provide a health category based on your BMI score.

Disclaimer

	• Health Buddy is an AI-powered advisor for general wellness guidance and should not be taken as medical advice.
	• Always consult a healthcare professional for medical decisions and specific health concerns.

### Empower your health journey with Health Buddy!
     
