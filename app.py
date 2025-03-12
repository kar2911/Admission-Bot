import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import streamlit.components.v1 as components

# Set page config
st.set_page_config(
    page_title="Admit Bot - College Admissions Assistant",
    page_icon="🎓",
    layout="wide"
)

# Title and Introduction
st.title("🎓 Admit Bot")
st.markdown("""
    Welcome to Admit Bot, your AI-powered college admissions assistant for Sathyabama Institute Of Science And Technology. 
    I'm here to help you navigate through college admissions, understand fee structures, 
    explore placement statistics, and provide personalized career counseling.
""")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Choose a section:",
    ["Home", "Admissions FAQ", "Fee Structure", "College Search", 
     "Student Counseling", "Parent Support", "Placement Statistics", "Virtual Campus Tour",
     "Student Counseling"]
)

if page == "Home":
    st.header("Welcome to Admit Bot!")
    st.markdown("""
        ### How can I help you today?
        
        1. **Admissions FAQ**: Get answers about deadlines, eligibility, and documents
        2. **Fee Structure**: Understand costs and payment plans
        3. **College Search**: Find colleges based on your preferences
        4. **Student Counseling**: Get personalized course recommendations
        5. **Parent Support**: Information for parents about ROI and facilities
        6. **Placement Statistics**: View career opportunities and packages
        
        Select a section from the sidebar to get started!
    """)

elif page == "Admissions FAQ":
    st.header("Admissions Information")
    
    # Create tabs for different admission aspects
    tab1, tab2, tab3, tab4 = st.tabs(["Deadlines", "Eligibility", "Documents", "Process"])
    
    with tab1:
        st.subheader("Important Deadlines")
        st.markdown("""
            ### Regular Admissions
            - Application Start: March 1, 2024
            - Last Date: May 31, 2024
            - Entrance Exam: June 15, 2024
            
            ### Early Admissions
            - Application Start: January 1, 2024
            - Last Date: February 28, 2024
            - Entrance Exam: March 15, 2024
        """)
        
        # Countdown to next deadline
        next_deadline = datetime(2024, 5, 31)
        days_left = (next_deadline - datetime.now()).days
        st.warning(f"⏰ {days_left} days left until regular admission deadline!")
    
    with tab2:
        st.subheader("Eligibility Criteria")
        course_type = st.selectbox("Select Course Type", 
            ["Engineering", "Medical", "Business", "Arts & Science"])
        
        if course_type == "Engineering":
            st.markdown("""
                ### Engineering Programs
                - Minimum 60% in PCM (Physics, Chemistry, Mathematics)
                - Valid JEE Main/Advanced score
                - Age: 17-25 years
            """)
        elif course_type == "Medical":
            st.markdown("""
                ### Medical Programs
                - Minimum 60% in PCB (Physics, Chemistry, Biology)
                - Valid NEET score
                - Age: 17-25 years
            """)
        # Add other course types...
    
    with tab3:
        st.subheader("Required Documents")
        st.markdown("""
            ### Essential Documents
            1. Academic Documents
                - 10th Mark Sheet
                - 12th Mark Sheet
                - Transfer Certificate
                - Migration Certificate
            
            2. Personal Documents
                - Passport size photographs
                - ID Proof (Aadhar/PAN)
                - Address Proof
            
            3. Additional Documents (if applicable)
                - Category Certificate (SC/ST/OBC)
                - Income Certificate
                - Sports Certificates
        """)
    
    with tab4:
        st.subheader("Application Process")
        st.markdown("""
            ### Step-by-Step Guide
            
            #### Step 1: Registration
            - Create account on admission portal
            - Fill basic details
            - Upload photo and signature
            
            #### Step 2: Application Form
            - Fill academic details
            - Choose preferred courses
            - Upload required documents
            
            #### Step 3: Entrance Exam
            - Register for entrance exam
            - Download admit card
            - Appear for exam
            
            #### Step 4: Counseling
            - Document verification
            - Course allocation
            - Fee payment
        """)

elif page == "Fee Structure":
    st.markdown("## Fee Structure and Financial Planning")
    
    # Course Selection with smaller headers
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Select Course Category")
        course_category = st.selectbox(
            "",  # Empty label since we're using markdown above
            ["Engineering", "Medical", "Business", "Arts & Science"]
        )
    
    with col2:
        st.markdown("#### Select Specific Course")
        if course_category == "Engineering":
            specific_course = st.selectbox(
                "",  # Empty label
                ["B.Tech - Computer Science and AI/ML", 
                 "B.Tech - Computer Science", 
                 "B.Tech - Electronics & Communication",
                 "B.Tech - Electrical Engineering",
                 "B.Tech - Mechanical Engineering"]
            )
        elif course_category == "Medical":
            specific_course = st.selectbox(
                "",
                ["MBBS", "BDS", "B.Pharm", "BSc Nursing"]
            )
        elif course_category == "Business":
            specific_course = st.selectbox(
                "",
                ["BBA - General", "BBA - Digital Marketing", 
                 "B.Com - Honours", "B.Com - Professional"]
            )
        else:
            specific_course = st.selectbox(
                "",
                ["BSc Computer Science", "BSc Mathematics", 
                 "BA Economics", "BA Psychology"]
            )

    # Fee Structure Display with enhanced visibility
    st.markdown("""
        <div style='background-color: #e6f3ff; padding: 15px; border-radius: 5px; margin: 10px 0;'>
            <h4 style='color: #0066cc; margin: 0;'>Annual Fee Breakdown</h4>
        </div>
    """, unsafe_allow_html=True)

    # Define fee structures
    fee_structures = {
        "B.Tech - Computer Science and AI/ML": {
            "Tuition Fee": 350000,
            "Development Fee": 50000,
            "Laboratory Fee": 35000,
            "Library Fee": 15000,
            "Technology Fee": 25000,
            "Student Activities": 15000,
            "Examination Fee": 10000,
            "Hostel Fee (Optional)": 120000,
            "Mess Fee (Optional)": 60000
        },
        "B.Tech - Computer Science": {
            "Tuition Fee": 300000,
            "Development Fee": 45000,
            "Laboratory Fee": 30000,
            "Library Fee": 15000,
            "Technology Fee": 20000,
            "Student Activities": 15000,
            "Examination Fee": 10000,
            "Hostel Fee (Optional)": 120000,
            "Mess Fee (Optional)": 60000
        }
        # Add other course fee structures as needed
    }

    # Get fee structure for selected course
    selected_fees = fee_structures.get(specific_course, {})
    if not selected_fees:
        selected_fees = {
            "Tuition Fee": 200000,
            "Development Fee": 30000,
            "Laboratory Fee": 20000,
            "Library Fee": 10000,
            "Student Activities": 10000,
            "Examination Fee": 8000,
            "Hostel Fee (Optional)": 100000,
            "Mess Fee (Optional)": 50000
        }

    # Display Fee Components with improved visibility
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.markdown("#### Fee Components")
        mandatory_total = 0
        optional_total = 0
        
        for fee_type, amount in selected_fees.items():
            if "Optional" in fee_type:
                optional_total += amount
                st.markdown(f"""
                    <div style='
                        background-color: #f8f9fa;
                        padding: 10px 15px;
                        border-radius: 5px;
                        margin: 8px 0;
                        border: 1px solid #dee2e6;
                        display: flex;
                        justify-content: space-between;
                        align-items: center;
                    '>
                        <span style='color: #666666; font-size: 16px;'>{fee_type}</span>
                        <span style='color: #666666; font-weight: 500; font-size: 16px;'>₹{amount:,}</span>
                    </div>
                """, unsafe_allow_html=True)
            else:
                mandatory_total += amount
                st.markdown(f"""
                    <div style='
                        background-color: white;
                        padding: 10px 15px;
                        border-radius: 5px;
                        margin: 8px 0;
                        border: 1px solid #dee2e6;
                        display: flex;
                        justify-content: space-between;
                        align-items: center;
                        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
                    '>
                        <span style='color: #000000; font-size: 16px;'>{fee_type}</span>
                        <span style='color: #000000; font-weight: 500; font-size: 16px;'>₹{amount:,}</span>
                    </div>
                """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### Fee Summary")
        st.markdown(f"""
            <div style='padding: 15px; border: 1px solid #dee2e6; border-radius: 5px;'>
                <p><strong>Mandatory Fees:</strong><br>₹{mandatory_total:,}</p>
                <p><strong>Optional Fees:</strong><br>₹{optional_total:,}</p>
                <p style='margin-top: 10px; border-top: 1px solid #dee2e6; padding-top: 10px;'>
                    <strong>Total Fees:</strong><br>₹{mandatory_total + optional_total:,}
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("#### Payment Breakdown")
        semester_fee = mandatory_total / 2
        monthly_fee = semester_fee / 6
        st.markdown(f"""
            <div style='padding: 15px; border: 1px solid #dee2e6; border-radius: 5px;'>
                <p><strong>Per Semester:</strong><br>₹{semester_fee:,.0f}</p>
                <p><strong>Monthly EMI*:</strong><br>₹{monthly_fee:,.0f}</p>
                <small style='color: #666666;'>*Approximate EMI with education loan</small>
            </div>
        """, unsafe_allow_html=True)

    # Simple Education Loan Details
    st.markdown("#### Education Loan Information")
    loan_col1, loan_col2 = st.columns(2)
    
    with loan_col1:
        st.markdown("""
            **Partner Banks**
            - State Bank of India (8.5% p.a.)
            - HDFC Bank (8.75% p.a.)
            - ICICI Bank (8.9% p.a.)
            - Axis Bank (9.0% p.a.)
        """)
    
    with loan_col2:
        st.markdown("""
            **Loan Benefits**
            - 100% financing available
            - No collateral up to ₹7.5 lakhs
            - Flexible repayment options
            - Tax benefits under Section 80E
        """)

    # Payment Options with smaller headers
    st.markdown("""
        <div style='background-color: #e6f3ff; padding: 15px; border-radius: 5px; margin: 20px 0;'>
            <h4 style='color: #0066cc; margin: 0;'>Payment Options</h4>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Payment Plans")
        payment_plans = {
            "One-time Payment": "5% discount on total fees",
            "Semester-wise": "No additional charges",
            "Quarterly": "2% additional charge",
            "Monthly": "3% additional charge"
        }
        
        for plan, detail in payment_plans.items():
            st.markdown(f"""
                <div style='
                    background-color: white;
                    padding: 10px 15px;
                    border-radius: 5px;
                    margin: 5px 0;
                    border: 1px solid #dee2e6;
                '>
                    <strong>{plan}</strong><br>
                    <small style='color: #666666;'>{detail}</small>
                </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### Available Scholarships")
        scholarships = {
            "Merit Scholarship": "Up to 50% waiver for >90% marks",
            "Sports Quota": "Up to 25% waiver for state/national players",
            "Girl Child": "Additional 10% waiver for female students",
            "Economic Background": "Up to 100% waiver based on family income"
        }
        
        for scheme, detail in scholarships.items():
            st.markdown(f"""
                <div style='
                    background-color: white;
                    padding: 10px 15px;
                    border-radius: 5px;
                    margin: 5px 0;
                    border: 1px solid #dee2e6;
                '>
                    <strong>{scheme}</strong><br>
                    <small style='color: #666666;'>{detail}</small>
                </div>
            """, unsafe_allow_html=True)

    # Financial Aid and Education Loan
    st.markdown("""
        <div style='background-color: #f0f2f6; padding: 20px; border-radius: 10px; margin: 20px 0;'>
            <h3 style='color: #1f77b4;'>Education Loan Assistance</h3>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Partner Banks")
        st.markdown("""
            - State Bank of India (8.85% p.a.)
            - HDFC Bank (9.50% p.a.)
            - ICICI Bank (9.85% p.a.)
            - Axis Bank (10.25% p.a.)
            
            *Interest rates are indicative and subject to change
        """)
    
    with col2:
        st.markdown("### Loan Benefits")
        st.markdown("""
            - 100% financing available
            - No collateral for loans up to ₹7.5 lakhs
            - Flexible repayment options
            - Tax benefits under Section 80E
            - Special rates for female students
        """)

    # Additional Information
    st.info("""
        📝 **Note:**
        - All fees are subject to revision
        - Additional charges may apply for specialized programs
        - Scholarships are subject to eligibility and availability
        - Education loan assistance is provided through the admission office
    """)

elif page == "College Search":
    st.header("College Search")
    
    # Simplified search filters
    col1, col2 = st.columns(2)
    with col1:
        main_stream = st.selectbox(
            "Select Your Stream of Interest",
            ["Engineering", "Medical", "Business", "Arts & Science"]
        )
    
    with col2:
        budget = st.slider("Annual Budget (in lakhs)", 0.0, 10.0, (2.0, 5.0))
    
    # Detailed course data with fees and eligibility
    engineering_courses = {
        "Computer Science and Engineering": {
            "annual_fee": 450000,
            "duration": "4 years",
            "eligibility": "PCM with 75%",
            "specializations": ["Regular CSE", "CSE with AI/ML", "CSE with Data Science"],
            "job_roles": ["Software Engineer", "Data Scientist", "AI Engineer"],
            "avg_package": "8.5 LPA",
            "description": "Core computer science fundamentals with programming and software development"
        },
        "CSE with AI/ML": {
            "annual_fee": 500000,
            "duration": "4 years",
            "eligibility": "PCM with 80%",
            "specializations": ["AI/ML", "Deep Learning", "Robotics"],
            "job_roles": ["AI Engineer", "ML Engineer", "Research Scientist"],
            "avg_package": "10 LPA",
            "description": "Advanced AI/ML concepts with hands-on projects and industry collaboration"
        },
        "Electronics and Communication": {
            "annual_fee": 300000,
            "duration": "4 years",
            "eligibility": "PCM with 70%",
            "specializations": ["VLSI", "Embedded Systems", "Communication Systems"],
            "job_roles": ["VLSI Engineer", "Hardware Engineer", "Network Engineer"],
            "avg_package": "6.5 LPA",
            "description": "Focus on electronic systems, communication technology, and circuit design"
        },
        "Electrical Engineering": {
            "annual_fee": 250000,
            "duration": "4 years",
            "eligibility": "PCM with 65%",
            "specializations": ["Power Systems", "Control Systems", "Electric Vehicles"],
            "job_roles": ["Power Engineer", "Design Engineer", "Systems Engineer"],
            "avg_package": "6 LPA",
            "description": "Study of electrical systems, power generation, and modern applications"
        }
    }

    medical_courses = {
        "MBBS": {
            "annual_fee": 900000,
            "duration": "5.5 years",
            "eligibility": "PCB with 85%",
            "specializations": ["General Medicine", "Surgery", "Pediatrics"],
            "job_roles": ["Doctor", "Surgeon", "Medical Officer"],
            "avg_package": "12 LPA",
            "description": "Complete medical education with clinical training and internship"
        },
        "BDS": {
            "annual_fee": 500000,
            "duration": "5 years",
            "eligibility": "PCB with 80%",
            "specializations": ["General Dentistry", "Orthodontics", "Oral Surgery"],
            "job_roles": ["Dentist", "Oral Surgeon", "Orthodontist"],
            "avg_package": "8 LPA",
            "description": "Comprehensive dental education with practical training"
        }
    }

    business_courses = {
        "BBA": {
            "annual_fee": 200000,
            "duration": "3 years",
            "eligibility": "Any stream with 60%",
            "specializations": ["Finance", "Marketing", "HR"],
            "job_roles": ["Business Analyst", "Marketing Manager", "HR Executive"],
            "avg_package": "5 LPA",
            "description": "Foundation in business management and administration"
        },
        "BBA with Digital Marketing": {
            "annual_fee": 300000,
            "duration": "3 years",
            "eligibility": "Any stream with 60%",
            "specializations": ["Digital Marketing", "Social Media", "E-commerce"],
            "job_roles": ["Digital Marketing Manager", "Social Media Analyst", "SEO Specialist"],
            "avg_package": "6 LPA",
            "description": "Modern business education with focus on digital marketing strategies"
        }
    }

    arts_science_courses = {
        "BSc Computer Science": {
            "annual_fee": 150000,
            "duration": "3 years",
            "eligibility": "Any stream with 60%",
            "specializations": ["Software Development", "Web Technologies", "Mobile Apps"],
            "job_roles": ["Software Developer", "Web Developer", "Technical Analyst"],
            "avg_package": "4.5 LPA",
            "description": "Computer science fundamentals with practical programming skills"
        },
        "BA Economics": {
            "annual_fee": 100000,
            "duration": "3 years",
            "eligibility": "Any stream with 55%",
            "specializations": ["Economic Analysis", "Finance", "Public Policy"],
            "job_roles": ["Economic Analyst", "Research Associate", "Policy Advisor"],
            "avg_package": "4 LPA",
            "description": "Study of economic theories, policies, and their applications"
        }
    }

    # Filter courses based on budget
    min_budget, max_budget = budget
    
    def get_eligible_courses(courses_dict, min_budget, max_budget):
        eligible_courses = {}
        for course, details in courses_dict.items():
            if min_budget * 100000 <= details["annual_fee"] <= max_budget * 100000:
                eligible_courses[course] = details
        return eligible_courses

    # Show relevant courses based on stream and budget
    st.subheader(f"Available Courses in {main_stream}")
    
    if main_stream == "Engineering":
        eligible_courses = get_eligible_courses(engineering_courses, min_budget, max_budget)
    elif main_stream == "Medical":
        eligible_courses = get_eligible_courses(medical_courses, min_budget, max_budget)
    elif main_stream == "Business":
        eligible_courses = get_eligible_courses(business_courses, min_budget, max_budget)
    else:
        eligible_courses = get_eligible_courses(arts_science_courses, min_budget, max_budget)
    
    if eligible_courses:
        for course, details in eligible_courses.items():
            with st.expander(f"📚 {course} - ₹{details['annual_fee']:,}/year"):
                st.markdown(f"*{details['description']}*")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("#### Course Details")
                    st.write(f"**Duration:** {details['duration']}")
                    st.write(f"**Eligibility:** {details['eligibility']}")
                    st.write(f"**Average Package:** {details['avg_package']}")
                
                with col2:
                    st.markdown("#### Specializations")
                    for spec in details['specializations']:
                        st.write(f"- {spec}")
                    
                    st.markdown("#### Career Opportunities")
                    for role in details['job_roles']:
                        st.write(f"- {role}")
    else:
        st.warning(f"No courses found in {main_stream} within the budget range of ₹{min_budget:.1f}-{max_budget:.1f} lakhs. Please adjust your budget.")

    # Additional Information
    if eligible_courses:
        st.subheader("Additional Benefits")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
                #### Scholarships Available
                - Merit-based scholarship (up to 50% waiver)
                - Sports quota scholarship
                - Girl child scholarship
                - Economic background scholarship
            """)
        
        with col2:
            st.markdown("""
                #### Campus Facilities
                - World-class laboratories
                - Digital library
                - Sports complex
                - Industry collaboration
                - Internship opportunities
            """)

elif page == "Student Counseling":
    st.header("Personalized Course Recommendations")
    
    # Get student information
    col1, col2 = st.columns(2)
    
    with col1:
        stream = st.selectbox("Select Your Stream", ["Science", "Commerce", "Arts"])
        percentage = st.number_input("Your 12th Percentage", 0.0, 100.0, 75.0)
        interests = st.multiselect(
            "Select Your Interests",
            ["Technology", "Healthcare", "Business", "Creative Arts", "Science", "Social Sciences"]
        )
    
    with col2:
        entrance_exam = st.selectbox("Entrance Exam Scores (if any)", 
            ["None", "JEE", "NEET", "CAT", "Other"])
        if entrance_exam != "None":
            exam_score = st.number_input("Enter your score/percentile", 0.0, 100.0, 50.0)
        
        strengths = st.multiselect(
            "Select Your Strengths",
            ["Mathematics", "Programming", "Biology", "Communication", "Creativity", "Analysis"]
        )
    
    if st.button("Get Recommendations"):
        st.success("Based on your profile, here are your recommended paths:")
        
        if stream == "Science" and percentage >= 60:
            st.markdown("""
                ### Primary Recommendations:
                
                1. **B.Tech in Computer Science**
                   - Your percentage qualifies you for top engineering colleges
                   - Strong job prospects (95% placement rate)
                   - Average package: 8-12 LPA
                   
                2. **B.Tech in Electronics**
                   - Growing field with IoT and automation
                   - 92% placement rate
                   - Average package: 7-10 LPA
            """)
        elif percentage < 60:
            st.markdown("""
                ### Alternative Pathways:
                
                1. **Diploma in Computer Applications**
                   - 3-year program
                   - Practical skill-based learning
                   - Option to upgrade to B.Tech later
                   
                2. **Vocational Training Programs**
                   - Web Development
                   - Digital Marketing
                   - Hardware Networking
            """)

elif page == "Parent Support":
    st.header("Information for Parents")
    
    tab1, tab2, tab3 = st.tabs(["ROI & Costs", "Campus Life", "Career Prospects"])
    
    with tab1:
        st.subheader("Return on Investment")
        
        # ROI Calculator
        course_cost = st.number_input("Total Course Cost (₹)", 500000, 2000000, 1000000)
        expected_salary = st.number_input("Expected Starting Salary (₹/year)", 300000, 1500000, 600000)
        years = st.slider("Years to Calculate ROI", 1, 10, 3)
        
        total_earnings = expected_salary * years
        roi = ((total_earnings - course_cost) / course_cost) * 100
        
        st.success(f"""
            ### ROI Analysis
            - Total Investment: ₹{course_cost:,}
            - Expected Earnings ({years} years): ₹{total_earnings:,}
            - ROI: {roi:.1f}%
            - Break-even Period: {course_cost/expected_salary:.1f} years
        """)
    
    with tab2:
        st.subheader("Campus Facilities & Safety")
        st.markdown("""
            ### Safety Measures
            - 24/7 Security Personnel
            - CCTV Surveillance
            - Biometric Access
            - Emergency Response Team
            
            ### Hostel Facilities
            - Separate hostels for boys and girls
            - 24/7 warden supervision
            - Modern amenities
            - Regular maintenance
            
            ### Medical Facilities
            - On-campus medical center
            - 24/7 medical staff
            - Ambulance service
            - Regular health check-ups
        """)
    
    with tab3:
        st.subheader("Career Opportunities")
        st.markdown("""
            ### Top Recruiters
            - Microsoft
            - Google
            - Amazon
            - IBM
            - TCS
            
            ### Industry Connections
            - Regular industry visits
            - Expert lectures
            - Internship opportunities
            - Industry projects
        """)

elif page == "Placement Statistics":
    st.header("Placement Statistics")
    
    # Sample placement data
    years = [2019, 2020, 2021, 2022, 2023]
    avg_salary = [8.5, 9.2, 10.5, 12.3, 14.2]
    placement_rate = [85, 88, 90, 92, 95]
    companies = [120, 135, 150, 175, 200]
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Salary trends
        fig1 = px.line(
            x=years, y=avg_salary,
            title="Average Package Trends (LPA)",
            labels={'x': 'Year', 'y': 'Average Package (LPA)'}
        )
        st.plotly_chart(fig1)
    
    with col2:
        # Placement rate
        fig2 = px.bar(
            x=years, y=placement_rate,
            title="Placement Rate (%)",
            labels={'x': 'Year', 'y': 'Placement Rate (%)'}
        )
        st.plotly_chart(fig2)
    
    # Top recruiters and packages
    st.subheader("Top Recruiters & Packages")
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("""
            ### Top Recruiters 2023
            1. Microsoft (25 LPA)
            2. Google (22 LPA)
            3. Amazon (20 LPA)
            4. Goldman Sachs (18 LPA)
            5. IBM (15 LPA)
        """)
    
    with col4:
        st.markdown("""
            ### Package Distribution
            - Highest Package: 45 LPA
            - Average Package: 14.2 LPA
            - Median Package: 12 LPA
            - Lowest Package: 6 LPA
        """)

elif page == "Virtual Campus Tour":
    st.header("360° Virtual Campus Tour - Sathyabama Institute")
    
    # Avatar Selection
    st.subheader("Customize Your Tour Experience")
    col1, col2 = st.columns(2)
    
    with col1:
        avatar = st.selectbox(
            "Choose Your Avatar",
            ["Student", "Parent", "Faculty", "Visitor"]
        )
        
    with col2:
        vehicle = st.selectbox(
            "Choose Your Transport",
            ["Walking", "Electric Cart", "Bicycle", "Segway"]
        )

    # Tour Starting Point Selection
    start_point = st.selectbox(
        "Select Your Starting Point",
        ["Main Gate", "Academic Block", "Library", "Hostels", "Sports Complex", "Labs"]
    )

    # Embed Campus Map and Tour
    st.markdown("### Begin Your Virtual Tour")
    st.markdown("Navigate through the campus using mouse or touch controls:")
    st.markdown("- **Left Click/Touch + Drag**: Look around")
    st.markdown("- **Right Click/Touch + Drag**: Move forward/backward")
    st.markdown("- **Scroll**: Zoom in/out")

    # Updated iframe with campus map
    components.html(
        """
        <div style="width:100%; height:600px; border:none; border-radius:10px; overflow:hidden;">
            <iframe 
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3890.040704806402!2d80.21832661482169!3d12.876655390918744!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a525b79de7f381b%3A0xffbb2dd48afe3f1b!2sSathyabama%20Institute%20of%20Science%20and%20Technology!5e0!3m2!1sen!2sin!4v1679940475043!5m2!1sen!2sin"
                width="100%" 
                height="100%" 
                style="border:0;" 
                allowfullscreen="" 
                loading="lazy" 
                referrerpolicy="no-referrer-when-downgrade">
            </iframe>
        </div>
        <style>
            iframe {
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }
        </style>
        """,
        height=620,
    )

    # Campus Gallery
    st.subheader("Campus Gallery")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("https://www.sathyabama.ac.in/sites/default/files/inline-images/campus1.jpg", 
                 caption="Main Building", use_column_width=True)
    with col2:
        st.image("https://www.sathyabama.ac.in/sites/default/files/inline-images/campus2.jpg", 
                 caption="Library Block", use_column_width=True)
    with col3:
        st.image("https://www.sathyabama.ac.in/sites/default/files/inline-images/campus3.jpg", 
                 caption="Academic Block", use_column_width=True)

    # Virtual Tour Points
    st.subheader("Virtual Tour Points")
    tour_points = {
        "Main Building": "Experience the grand entrance and administrative block with modern architecture and state-of-the-art facilities",
        "Academic Block": "Explore our modern classrooms and lecture halls equipped with smart learning technologies",
        "Central Library": "Visit our extensive library with digital resources, reading halls, and research sections",
        "Research Centers": "Discover advanced research facilities and cutting-edge laboratories",
        "Sports Complex": "Tour our world-class sports facilities including indoor and outdoor courts",
        "Hostel Block": "View our comfortable student accommodation with modern amenities"
    }

    for point, description in tour_points.items():
        st.markdown(f"""
            <div style='
                padding: 15px;
                border: 1px solid #ddd;
                border-radius: 5px;
                margin: 10px 0;
                background-color: white;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            '>
                <strong style='color: #1f77b4; font-size: 18px;'>{point}</strong><br>
                <p style='margin-top: 8px; color: #444;'>{description}</p>
            </div>
        """, unsafe_allow_html=True)

    # Tour Highlights
    st.subheader("Campus Highlights")
    
    highlights = {
        "Academic Facilities": [
            "State-of-the-art classrooms",
            "Modern laboratories",
            "Central library with digital resources",
            "Research centers"
        ],
        "Infrastructure": [
            "Wi-Fi enabled campus",
            "Smart classrooms",
            "Advanced research labs",
            "Modern auditorium"
        ],
        "Sports & Recreation": [
            "Olympic-size swimming pool",
            "Indoor sports complex",
            "Outdoor sports fields",
            "Fitness center"
        ],
        "Student Amenities": [
            "Modern hostels",
            "Food court",
            "Medical center",
            "Banking facility"
        ]
    }

    col1, col2 = st.columns(2)
    
    with col1:
        for title in list(highlights.keys())[:2]:
            st.markdown(f"#### {title}")
            for item in highlights[title]:
                st.markdown(f"- {item}")
            st.markdown("<br>", unsafe_allow_html=True)
    
    with col2:
        for title in list(highlights.keys())[2:]:
            st.markdown(f"#### {title}")
            for item in highlights[title]:
                st.markdown(f"- {item}")
            st.markdown("<br>", unsafe_allow_html=True)

    # Quick Navigation
    st.subheader("Quick Navigation")
    quick_nav = st.multiselect(
        "Jump to Specific Locations",
        ["Main Building", "Library", "Hostels", "Cafeteria", "Sports Complex", 
         "Laboratories", "Auditorium", "Medical Center", "Transport Hub"]
    )

    # Tour Guide
    if st.checkbox("Enable Virtual Tour Guide"):
        st.info("""
            Your virtual guide will provide detailed information about each location 
            as you navigate through the campus. Enable audio for the best experience.
        """)

    # Additional Information
    st.markdown("### Additional Information")
    st.markdown("""
        - Tour is best viewed on a desktop/laptop
        - Use headphones for an immersive experience
        - Virtual tour is available 24/7
        - For technical support, contact: support@sathyabama.ac.in
    """)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        <p>© 2024 Admit Bot | Contact: support@admitbot.com</p>
    </div>
""", unsafe_allow_html=True)