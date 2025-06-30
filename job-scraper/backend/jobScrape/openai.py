
def extract_skills(description, chain):
    return chain.invoke({
        "description": description + "give short summary of responsibilities and skills i would need"
    })

# template = """
# description: {description}

# Answer:
# """

# model = OllamaLLM(model="llama3.2")
# prompt = ChatPromptTemplate.from_template(template)
# chain = prompt | model

# description = """Nightwing provides technically advanced full-spectrum cyber, data operations, systems integration and intelligence mission support services to meet our customers’ most demanding challenges. Our capabilities include cyber space operations, cyber defense and resiliency, vulnerability research, ubiquitous technical surveillance, data intelligence, lifecycle mission enablement, and software modernization. Nightwing brings disruptive technologies, agility, and competitive offerings to customers in the intelligence community, defense, civil, and commercial markets.

# You have been redirected to RTX’s career page as we have recently transitioned from RTX to become a standalone company, which provides us with greater autonomy and opportunities for growth. As a prospective employee of Nightwing, you’ll have the chance to contribute to our continued success and shape the future of our cybersecurity, intelligence, and services offerings. Job Summary We are seeking a qualified software developer (SWE1) to support modernization and development of next generation cybersecurity software. The ideal candidate will help design and develop cutting edge, modern and scalable frameworks for our customers to ensure our customers have the latest and greatest technologies available to the warfighter. Projects are worked directly with customers on the most mission critical systems to quickly enhance capabilities or resolve issues in existing tools for real-world applications. Role Type This position is an onsite role. Basic Qualifications: Typically requires Bachelor’s degree in Computer Science or related discipline from an accredited college or university and 7 years experience and experience with C, C++, or Python Analyze user requirements to derive software design and performance requirements. Debug existing software and correct defects. Provide recommendations for improving documentation and software development process standards. Design and code new software or modify existing software to add new features. Integrate existing software into new or modified systems or operating environments. Design or implement complex database or data repository interfaces/queries Active and transferable U.S. government issued TS/SCI with polygraph security clearance is required prior to start date. U.S. citizenship is required, as only U.S. citizens are eligible for a security clearance. What We Offer: Whether you’re just starting out on your career journey or are an experienced professional, we offer a total rewards package that goes above and beyond with compensation; healthcare, wellness, retirement and work/life benefits; career development and recognition programs. Some of the benefits we offer include parental (including paternal) leave, flexible work schedules, achievement awards, educational assistance and child/adult backup care. Previously part of a leading Fortune 100 company and headquartered in Dulles, VA; Nightwing became independent in 2024 but continues to support the nation’s most mission impactful initiatives. When we formed Nightwing, we brought a deep set of credentials and an unfaltering commitment to the mission. For over four decades, our team has been providing some of the world’s most technically advanced full-spectrum cyber, data operations, systems integration and intelligence support services to the U.S. government on its most important missions. At Nightwing, we value collaboration and teamwork. You’ll have the opportunity to work alongside talented individuals who are passionate about what they do. Together, we’ll leverage our collective expertise to drive innovation, solve complex problems, and deliver exceptional results for our clients. Thank you for considering joining us as we embark on this new journey and shape the future of cybersecurity and intelligence together as part of the Nightwing team. #NWTGSWE1

# At Nightwing, we value collaboration and teamwork. You’ll have the opportunity to work alongside talented individuals who are passionate about what they do. Together, we’ll leverage our collective expertise to drive innovation, solve complex problems, and deliver exceptional results for our clients.

# Thank you for considering joining us as we embark on this new journey and shape the future of cybersecurity and intelligence together as part of the Nightwing team.

# Nightwing is An Equal Opportunity/Affirmative Action Employer. All qualified applicants will receive consideration for employment without regard to race, color, religion, sex, sexual orientation, gender identity, national origin, disability or veteran status, age or any other federally protected class."""

# result = chain.invoke({"description": description + " can you make a bulletpoint of skills I would need for this job"})
# print(result)