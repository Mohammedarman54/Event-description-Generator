### **📌 Event Description Generator**  
**Generate professional event descriptions and promotional content effortlessly!**  

![Event Generator Banner](https://source.unsplash.com/1000x400/?event,technology)  

---

## **📖 About the Project**  
The **Event Description Generator** is a web-based tool designed to help **event planners** create compelling event descriptions and promotional content.  
It leverages **AI-powered text generation** to produce engaging and professional event write-ups in seconds.  

### **✨ Features:**  
✅ **AI-Powered** – Uses NLP to generate event descriptions.  
✅ **Easy-to-Use Interface** – Simple form-based input.  
✅ **Real-time Generation** – Instantly creates content.  
✅ **Customizable Tone & Style** – Tailored for different event types.  

---

## **⚙️ Technologies Used**  
- **Frontend:** HTML, CSS (Enhanced UI with Glassmorphism)  
- **Backend:** FastAPI (Python)  
- **API Integration:** iVis Labs API for text generation  
- **Deployment:** GitHub, Render/Vercel (Optional)  

---

## **🚀 How to Set Up Locally**  
### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/Mohammedarman54/Event-description-Generator.git
cd Event-description-Generator
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**  
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### **3️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4️⃣ Run the Application**  
```bash
uvicorn main:app --reload
```

🎯 The app will be live at **http://127.0.0.1:8000/**  

---

## **🛠 API Endpoints**  
| Method | Endpoint | Description |
|--------|---------|-------------|
| **GET** | `/` | Loads the homepage |
| **POST** | `/generate` | Generates an event description |

---

## **📸 Screenshots**  
### **🔹 Input Form**  
![Input Form](https://source.unsplash.com/600x300/?form,technology)  

### **🔹 Generated Event Description**  
![Generated Event](https://source.unsplash.com/600x300/?technology,conference)  

---

## **📜 Example Input & Output**  
### **📝 Input (Form Data)**
```json
{
    "event_name": "Tech Vision 2025",
    "date": "April 15, 2025",
    "location": "Bangalore International Convention Centre, India",
    "audience": "Software Developers, AI Enthusiasts, IT Professionals",
    "key_attractions": "AI Workshops, Industry Experts, Live Demos, Networking Sessions",
    "event_type": "Formal"
}
```

### **✅ Output (Generated Description & Social Media Post)**
```json
{
    "event_description": "Join us at Tech Vision 2025 on April 15 at the Bangalore International Convention Centre! Dive into the future of technology with cutting-edge AI workshops, insightful talks by industry experts, live demos, and networking opportunities. Be part of the next big tech revolution!",
    
    "social_media_post": "🚀 Exciting News! Tech Vision 2025 is happening on April 15 in Bangalore! Don't miss AI workshops, live demos & expert talks. Stay ahead in tech! 🔥 #TechVision2025 #AIInnovation #Networking"
}
```

---

## **🔗 Live Demo**  
🚀 **[Try it Live](https://your-deployment-url.com/)** *(If deployed)*  

---

## **🤝 Contributing**  
**Want to improve this project?**  
1️⃣ Fork the repository.  
2️⃣ Create a new branch (`feature-branch`).  
3️⃣ Commit changes (`git commit -m "New feature added"`).  
4️⃣ Push & create a Pull Request.  

---

## **📜 License**  
This project is **MIT Licensed**. Feel free to use and improve it.  

---

### **🔗 Connect with Me**  
📌 **GitHub:** [Mohammed Arman Ali](https://github.com/Mohammedarman54)  
📌 **LinkedIn:** [Mohammed Arman Ali](https://www.linkedin.com/in/mohammed-arman-ali-b58829258/)  

