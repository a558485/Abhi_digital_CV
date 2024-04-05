from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Abhishek Pardeshi"
PAGE_ICON = "👩‍💻"
NAME = "Abhishek Pardeshi"
DESCRIPTION = """
1. Cybersecurity/ Technology Risk Manager/ Auditor
2. Novice Python Developer
3. Developing web applications for Cybersecurity using AI and Data Science 
"""
EMAIL = "abhipardeshi22@outlook.com"
SOCIAL_MEDIA = { 
    "LinkedIn": "https://www.linkedin.com/in/abhishek-pardeshi-89a74437/",
    "GitHub": "https://github.com/a558485"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,layout="wide")


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2, col3 = st.columns(spec=[0.3,0.3,0.5], gap="medium",)
with col1:
    st.write(' ')

with col2:
    st.image(profile_pic, width=250)

with col3:
    st.title(NAME,)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    # --- SOCIAL LINKS ---
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")






# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Profile Summary")
st.write(
    """
- ✔️ Experienced Cybersecurity & IT Security professional with more than 11 years of experience
- ✔️ Specialises in managing, leading and delivering Cybersecurity risk assessments, Cloud Security assessments, Red Team testing, Technology Risk oversight, control testing and assurance. 
- ✔️ Extensive experience working in financial services sector including banking, insurance and asset management companies
- ✔️ Experience of working in all the 3 Lines of Defense
- ✔️ Experience in managing relationships with senior stakeholders as well as challenging and influencing technical SMEs
- ✔️ Performed effective oversight over multi-million dollar projects to ensure appropriate risk mitigation and sustainable control implementation
- ✔️ Managed multi-disciplinary teams with line management responsibilities
"""
)

st.subheader("Education")
st.write(
    """
 🎓Bachelor of Technology (Electronics) | Veermata Jijabai Technological Institute (VJTI, Mumbai) (2007 - 2011)
 
 🎓Masters of Business Administration (Marketing & Finance) | Symbiosis International University (SIU. Pune) (2011 - 2013) 
"""
)
# --- Certifications ---
st.write('\n')
st.subheader("Certifications")
st.write(
    """
- 🥇 [Certified Information Systems Auditor(CISA)](https://www.credly.com/earner/earned/badge/b311c6d5-6620-46b0-83a5-1775a7bb0128)
- 🥇 [Certified Cloud Security Practinor(CCSP)](https://www.credly.com/earner/earned/badge/78f00799-c272-49aa-a21c-e92fc6926f17)
- 🥇 [SC-900: Microsoft certified Security, Compliance & Identity Fundamentals](https://www.credly.com/earner/earned/badge/523caeb0-d5f7-4538-ad97-62d5507895a3)
- 🥇 [AZ-900: Azure Fundamentals](https://www.credly.com/earner/earned/badge/f81aafed-2eec-4cde-a92c-a69fba8e9423)
- 🥇 [AI-900: Azure AI Fundamentals](https://www.credly.com/earner/earned/badge/6ac88003-6bdc-4553-807a-030848f4ca3d)
- 🥇 AWS Security Fundamentals
- 🥇 [API Security Fundamentals](https://www.credly.com/earner/earned/badge/a471d1f4-193d-4fea-9003-cdfb09082cea)
- 🥇 [AttackIQ Foundations of Breach & Attack Simulation](https://www.credly.com/earner/earned/badge/9b7f1f60-284a-421b-9ab7-4bca3aec6ff4)
- 🥇 [AttackIQ Uniting Threat and Risk Management with NIST 800-53 and MITRE ATT&CK](https://www.credly.com/earner/earned/badge/e62ef6f0-1f92-4d7c-9fbb-46611984cfdc)
- 🥇 Attacking Windows Active Directory Certification(Tryhackme)
- 🥇 CyberArk Trustee
- 🥇 CREST Cybersecurity Security Analyst (CPSA)
- 🥇 Certified Red Team Professional (CRTP)
- 🥇 Certified Azure Web Application Security Professional
"""
)

# --- WORK HISTORY ---
st.subheader("Work History")

# --- JOB 1

st.write("🚧", "**Cyber Risk Manager | Natwest Group (02/2022 - Present)**")
st.write(
    """
- 🟢 Responsible for managing relationships with Security Leadership team along with Directos of Risks, audit and provide pragmatic challenge and oversight over security projects/ activities
- 🟢 Led Cloud Security assessment of AWS and GCP platforms to identify risks and issues across access management, vulnerability management, asset management, security monitoring and governance, risk & compliance and agree remedial actions
- 🟢 Led security deep dives across areas like DevSecOps, Internet facing sites, Vulnerability management, Ransomware preparedness & response, AD and Service Account Security, Infrastrcuture Privilege Access Management, Generative AI and Cyber Risk Quantification. Provided risk opinions and influenced security and technology decisions to ensure effective risk mitigation
- 🟢 Led the development and implementation of GenAI risk assessment process, updating risk management policy through liasion with various Security, Engineering, Risk, Audit colleagues and aligning to standards and best practice
- 🟢 Led the development and implementation of Security risk dashboards to perform oversight and challenge using Tableau and ServiceNow
- 🟢 Provide oversight and challenge over various key security programs like cyber risk quantification, EDR deployment, DLP deployment, CASB implementation, cloud security monitoring and cyber threat intelligence
- 🟢 Performed external benchmarking and internal data analysis to influence and define security RAMs and KRIs
- 🟢 Provide risk opinions at various 1LOD and 2LOD Risk forums and represent 2LOD at various risk committees and working groups"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Cyber Risk Consultant | M&G (08/2019 - 01/2022)**")
st.write(
    """
- 🟢 Responsible for managing relationships with senior stakeholders in Security/ Technology and mentoring junior members of the team.
- 🟢 Successfully managed a budget of £100k and delivered “Threat Intel baseed Red Team" testing capability (Cyber Assurance Testing) to periodically test M&G’s preparedness to prevent, detect and respond to cyber threats
- 🟢 Successfuly established and managed Red Team capability through vendor due-deligence, contract negotiation, scoping, test management, delivery, reporting and issue closure. Successfully established a sustainable process to test organisational security controls with 50% cost reduction and improving cyber prevention/ detection capabilities by over 60%
- 🟢 Performed risk based reviews of security areas like Vulnerability Assessment, Security Security Configuration Baselines, Endpoint Detection & Respone, Privileged Access Management, Application Security, etc. Delivered timely reports and agreed actions with Senior Stakeholders as well as Technical SMEs.
- 🟢 Tracked and monitored the risk review actions to closure through regular and proactive engagement with the action owners
- 🟢 Provided continuous oversight on Strategic Security program/ projects, perform risk based reviews, produce risk opinions and provide recommendations to ensure benefits realisation and risk reduction through the projects/ programs
- 🟢 Reviewed various cyber strategies like Security Operations, Cyber Threat Intel, Identitity & Access Management, Application Secuirty, etc. and provided risk opinion
- 🟢 Provided regular oversight of cyber incidents, operational IT incidents and other risk events to ensure appropriate actions are taken for remediation
- 🟢 Performed risk assessments for technology changes, incidents, security vulnerabilities , supporting international offices and provide appropriate challenge during risk acceptances/ mitigation to ensure risks are kept within pproved appetite
- 🟢 Facilitated ISO27001 compliance through internal attestation and external audit management
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Principal IT Auditor | M&G (02/2017 - 07/2019)**")
st.write(
    """
- 🟢 Responsible for leading & delivering cybersecurity reviews, IT infrastructure audits including cloud, application controls and ITGC controls reviews across Aladdin application and various front, middle & back office applications
- 🟢 Responsible for managing stakeholder relationships across security and IT infrastructure team
- 🟢 Performed various audits including Cyber Incident Response review, Project management reviews, API Security review, SaaS Governance & Security revie, GDPR readiness review, Exchange Online and Intune Office 365 security review and SSH data transfer controls review
- 🟢 Responsible for identifying emerging technology/ security risks within the organisation and proposing audit review in the annual plan.
- 🟢 Worked on numerous integrated audits like Equity Dealing Desk, Stock Lending, Corporate Actions, Fixed Income Dealing, etc. and assessed Technology related risks & controls.
- 🟢 Delivered audit reports with executive summary, detailed observations, actions and agreed timelines with action owners. Reviewed workpapers drafted by junior team members and provided appropriate feedback which aligned with internal audit methodology
- 🟢 Tracked and monitored the audit actions to closure through regular and proactive engagement with the action owners
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Cybersecurity Consultant | PwC (08/2014 - 01/2017)**")
st.write(
    """
- 🟢 Performed gap assessment of current network architecture, current security solution implementation and policy & procedure using ISF framework & ISO 27001 controls and came up maturity rating. Drafted policy & procedure around information security. Prepared cybersecurity roadmap consisting of to be network architecture and entire universe of security solution with implementation timelines
- 🟢 Managed & delivered 'Application security framework' for Global Information Security team. This framework was developed in alignment with OWASP Enterprise Application Security Project (OWASP-EASI), ISO 27034, NIST’s SP800-27, SP800-64 (Security Considerations in the Information System Development Life Cycle) and corporate security policy. Developed Threat modelling guidelines to arrive at application specific threat trees to help identify & mitigate vulnerabilities proactively
- 🟢 Performed vulnerability assessments and security configuration reviews for IT infrastructure elements including servers, routers and switches and penetration testing for web applications.
- 🟢 Managed & led IT general controls audits comprising of access management, incident management, backup and log management, physical & environmental security, change management, patch management, information exchange, asset lifecycle management and Scrum.
"""
)
st.write('\n')
st.write("🚧", "**Assistant Manager - Business Transformation & SLA Governance | Atos (04/2013 - 08/2014)**")
st.write(
    """
- 🟢 Developed policy, processes and procedure with appropriate roles & responsibilities and SLA KPIs for each process. It also involved process walkthrough with senior management and other relevant stakeholders
- 🟢 Desgined Roles &Responsibilities for incident management and problem management process, performing process gap analysis for as-is IT operational processes and design to-be process, aligning IT processes with respect to ITIL processes
"""
)
# --- Projects & Accomplishments ---
