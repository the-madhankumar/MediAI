from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak

# File path
pdf_path = "./Medical_Report.pdf"

# Create document
doc = SimpleDocTemplate(pdf_path, pagesize=A4)
styles = getSampleStyleSheet()
story = []

# Title
title_style = ParagraphStyle('Title', fontSize=18, alignment=1, spaceAfter=20, textColor=colors.HexColor("#004B8D"))
story.append(Paragraph("Comprehensive Health Diagnostic Report", title_style))
story.append(Spacer(1, 12))

# Patient Info
info = """
<b>Patient Name:</b> Aarav Sharma<br/>
<b>Age:</b> 36 years<br/>
<b>Gender:</b> Male<br/>
<b>Patient ID:</b> MSR-2025-0147<br/>
<b>Date of Report:</b> 22-Oct-2025<br/>
<b>Referring Doctor:</b> Dr. Nisha Varma<br/>
<b>Laboratory:</b> CityCare Diagnostics, Bangalore<br/>
"""
story.append(Paragraph(info, styles["Normal"]))
story.append(Spacer(1, 12))

# Table of Results (Detailed)
data = [
    ["Test Name", "Result", "Normal Range", "Units"],
    ["Hemoglobin", "13.8", "13.0 – 17.0", "g/dL"],
    ["RBC Count", "4.9", "4.5 – 5.9", "million/µL"],
    ["WBC Count", "8,200", "4,000 – 11,000", "/µL"],
    ["Platelet Count", "3.2", "1.5 – 4.5", "lakh/µL"],
    ["Fasting Blood Sugar", "112", "70 – 110", "mg/dL"],
    ["Postprandial Blood Sugar", "155", "<140", "mg/dL"],
    ["HbA1c", "6.1", "<5.7", "%"],
    ["Total Cholesterol", "228", "<200", "mg/dL"],
    ["LDL Cholesterol", "142", "<100", "mg/dL"],
    ["HDL Cholesterol", "38", ">40", "mg/dL"],
    ["Triglycerides", "182", "<150", "mg/dL"],
    ["SGPT (ALT)", "42", "10 – 40", "U/L"],
    ["SGOT (AST)", "39", "10 – 40", "U/L"],
    ["Alkaline Phosphatase", "88", "40 – 120", "U/L"],
    ["Total Bilirubin", "0.8", "0.3 – 1.2", "mg/dL"],
    ["Serum Creatinine", "1.1", "0.6 – 1.3", "mg/dL"],
    ["Uric Acid", "6.8", "3.4 – 7.0", "mg/dL"],
    ["Calcium", "9.3", "8.6 – 10.2", "mg/dL"],
    ["Vitamin D (25-OH)", "24", "30 – 100", "ng/mL"],
    ["Vitamin B12", "276", "200 – 900", "pg/mL"],
    ["TSH", "3.5", "0.4 – 4.0", "µIU/mL"],
    ["Free T3", "3.1", "2.0 – 4.4", "pg/mL"],
    ["Free T4", "1.1", "0.8 – 1.8", "ng/dL"],
]

table = Table(data, hAlign='LEFT', colWidths=[160, 90, 140, 70])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#004B8D")),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
]))
story.append(table)
story.append(Spacer(1, 18))

observations = """
<b>Summary:</b><br/>
The patient’s lipid profile indicates elevated total cholesterol and LDL cholesterol with low HDL, signifying an imbalance that could increase cardiovascular risk.
Blood glucose and HbA1c levels indicate early-stage prediabetes. Vitamin D and B12 deficiencies are also noted, suggesting poor nutrient absorption or limited sun exposure.
Liver and kidney function tests remain within acceptable ranges. Thyroid levels are normal.<br/><br/>
"""
story.append(Paragraph(observations, styles["Normal"]))
story.append(PageBreak())

# Page 2 - Extended Recommendations and Health Advice
story.append(Paragraph("Detailed Doctor Review & Lifestyle Plan", title_style))
story.append(Spacer(1, 12))

details = """
<b>Doctor's Observation:</b> <br />
The patient’s overall health is stable but trending toward metabolic imbalance.
Immediate lifestyle modifications and nutritional supplements are advised to prevent chronic conditions. <br /> <br />

<b>Clinical Analysis:</b><br/>
The biochemical markers indicate potential metabolic stress characterized by high lipid levels and slightly elevated blood glucose. These patterns are consistent with early metabolic syndrome.
If unaddressed, the patient could develop insulin resistance and cardiovascular complications. The vitamin deficiencies, though mild, contribute to fatigue, low energy, and occasional muscle weakness.<br/><br/>

<b>Dietary Guidance:</b><br/>
1. Include high-fiber foods such as oats, lentils, beans, and fresh vegetables.<br/>
2. Avoid refined sugars, fried foods, and processed snacks.<br/>
3. Incorporate healthy fats (olive oil, nuts, avocados) in moderation.<br/>
4. Consume fatty fish (salmon, tuna) twice weekly for omega-3 benefits.<br/>
5. Limit red meat consumption to once per week.<br/>
6. Reduce salt intake below 5g per day.<br/><br/>

<b>Exercise & Lifestyle:</b><br/>
1. Engage in brisk walking or jogging for at least 30 minutes daily.<br/>
2. Include strength training twice a week to improve metabolism.<br/>
3. Ensure at least 7 hours of restful sleep every night.<br/>
4. Maintain consistent hydration of 2.5–3 liters of water per day.<br/>
5. Practice mindfulness or yoga to reduce stress-induced hormonal changes.<br/><br/>

<b>Supplement Recommendations:</b><br/>
1. Vitamin D3 (1000 IU daily) for 3 months.<br/>
2. Vitamin B12 (500 mcg weekly) or as prescribed.<br/>
3. Omega-3 fatty acid supplement (1000 mg daily).<br/>
4. Multivitamin tablet once daily post-meal.<br/><br/>

<b>Follow-Up Instructions:</b><br/>
Re-evaluation recommended after 3 months with fasting lipid profile, blood sugar, and vitamin levels.
Immediate consultation is advised if symptoms like excessive thirst, frequent urination, or chest discomfort occur.<br/><br/>

<b>Doctor’s Signature:</b> ___________________________<br/>
<b>Doctor Name:</b> Dr. Nisha Varma, MD (Internal Medicine)<br/>
<b>Clinic:</b> CityCare Diagnostics, Bangalore<br/>
<b>Date:</b> 22-Oct-2025<br/>
"""
story.append(Paragraph(details, styles["Normal"]))

# Build PDF
doc.build(story)

pdf_path
