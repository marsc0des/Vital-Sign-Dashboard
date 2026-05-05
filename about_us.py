import taipy.gui.builder as tgb
from components.navbar import navbar

with tgb.Page() as about_us:
    navbar()

    with tgb.part(class_name="page-header"):
        tgb.text("About VI-Wave", class_name="title")

    #Project Overview 
    with tgb.part(class_name="card"):
        tgb.text("Project Overview", class_name="card-title")
        tgb.text(
            "     The purpose of Vi-Wave is to present a non-contact vital sign monitoring system that will " 
            "effectively retrieve human echocardiogram signals, heart rate, and respiratory rate, leveraging " 
            "millimeter wave Radar technology by the Doppler effect.", class_name="card-body-text"
        )
        tgb.text(
            "     The system uses the MMWAVEICBOOST development platform in conjunction with Texas Instruments " 
            "IWR6843AOP radar module operating at 60 GHz to detect minute chest displacements caused by breathing "
            "and cardiac micro-motions. Advanced signal-processing techniques are used to analyze these movements "
            "and produce precise, real-time vital-sign outputs. Vi-Wave's overarching objective is to provide a " 
            "monitoring platform that is safe, accurate, and easy to use for emergency responders, hospitals, home " 
            "care settings, and global health applications. ",
            class_name="card-body-text"
        )

    #Technology 
    with tgb.part(class_name="card"):
        tgb.text("Technology", class_name="card-title")
        with tgb.layout("1 1"):
            with tgb.part(class_name="tech-card"):
                tgb.text("Millimeter Wave Radar", class_name="tech-title")
                tgb.text(
                    "mmWave radar operates in the 60–77 GHz frequency range, allowing it to detect "
                    "sub-millimeter movements. This enables accurate capture of chest wall oscillations "
                    "caused by cardiac and respiratory activity.",
                    class_name="tech-desc"
                )
            with tgb.part(class_name="tech-card"):
                tgb.text("Doppler Effect Processing", class_name="tech-title")
                tgb.text(
                    "The system applies Doppler signal processing to extract periodic motion patterns "
                    "from raw radar returns. Frequency components corresponding to heart rate and "
                    "breathing rate are isolated and quantified.",
                    class_name="tech-desc"
                )
            with tgb.part(class_name="tech-card"):
                tgb.text("Signal Processing Pipeline", class_name="tech-title")
                tgb.text(
                    "Raw radar data undergoes range-FFT, Doppler-FFT, and phase extraction stages "
                    "before being passed through bandpass filters tuned to physiological frequency bands.",
                    class_name="tech-desc"
                )
            with tgb.part(class_name="tech-card"):
                tgb.text("Data Logging & Visualization", class_name="tech-title")
                tgb.text(
                    "Processed vital sign data is timestamped and logged to CSV format for "
                    "offline analysis. This dashboard provides real-time visualization and "
                    "health status interpretation.",
                    class_name="tech-desc"
                )

    # Research Objectives
    with tgb.part(class_name="card"):
        tgb.text("Research Objectives", class_name="card-title")
        with tgb.layout("1 1"):
            with tgb.part(class_name="objective-card"):
                tgb.text("01 — Accurate Vital Sign Extraction", class_name="objective-title")
                tgb.text(
                    "Validate that mmWave radar can reliably extract heart rate and respiratory rate "
                    "within clinically acceptable error margins compared to reference sensors.",
                    class_name="objective-desc"
                )
            with tgb.part(class_name="objective-card"):
                tgb.text("02 — Non-Contact Operation", class_name="objective-title")
                tgb.text(
                    "Demonstrate effective monitoring at a practical standoff distance without "
                    "any wearables, electrodes, or physical contact with the subject.",
                    class_name="objective-desc"
                )
            with tgb.part(class_name="objective-card"):
                tgb.text("03 — Accessible Health Insights", class_name="objective-title")
                tgb.text(
                    "Build a user-facing application that translates raw radar data into "
                    "actionable, personalized health insights for non-expert users.",
                    class_name="objective-desc"
                )
            with tgb.part(class_name="objective-card"):
                tgb.text("04 — Scalable Platform", class_name="objective-title")
                tgb.text(
                    "Design a modular software architecture that can be extended to support "
                    "additional biometric signals, multiple radar units, and cloud integration.",
                    class_name="objective-desc"
                )

    #Operating Environments + intended Use/users
    with tgb.part(class_name="card"):
        tgb.text("Operation", class_name="card-title")
        tgb.text("The operating environment of our system plays a vital role in its effectiveness, as it depends " 
        "heavily on the intended use. Whether the purpose is fitness performance enhancement, sleep monitoring, " 
        "hospital applications, or first responder contexts, the device can adapt to a wide range of conditions. " 
        "Because it is designed for portability, the system can also function reliably in environments where external " 
        "factors may influence its accuracy.", class_name="card-body-text")

    with tgb.part(class_name="card"):
        tgb.text("Intended User(s)", class_name="card-title")
        tgb.text("The system is designed to assist a wide range of end users in emergency and healthcare settings. " 
        "The important organizations that might profit from the installation of a contactless, radar-based cardiac " 
        "monitoring system are as follows: ", class_name="card-body-text")  
        with tgb.layout("1 1"):
            with tgb.part(class_name="tech-card"):
                tgb.text("Hospitals", class_name="tech-title")
                tgb.text(
                    "A non-invasive cardiac monitoring device that eases patient pain and streamlines " 
                    "ongoing monitoring would be advantageous for hospitals and clinical settings. ",
                    class_name="tech-desc"
                )
            with tgb.part(class_name="tech-card"):
                    tgb.text("Data Logging & Visualization", class_name="tech-title")
                    tgb.text(
                        "In situations when anchoring electrodes is impractical, portable deployment " 
                        "enables paramedics and emergency medical technicians (EMTs) to evaluate heart activity " 
                        "on-site rapidly. ",
                        class_name="tech-desc"
                    )
            with tgb.part(class_name="tech-card"):
                    tgb.text("Burn Patients", class_name="tech-title")
                    tgb.text(
                        "Adhesive electrodes are frequently intolerable to those who are severely burned. A " 
                        "contactless system provides a secure alternative to skin-irritating monitoring. ",
                        class_name="tech-desc"
                    )
            with tgb.part(class_name="tech-card"):
                    tgb.text("Neurodivergent Patients", class_name="tech-title")
                    tgb.text(
                        "Traditional wired monitoring may be resisted by patients with increased sensory sensitivity, "
                        "such as those on the autistic spectrum. By avoiding immediate contact, a radar-based technology " 
                        "helps lower stress levels. ",
                        class_name="tech-desc"
                    )
    with tgb.part(class_name="card"):
        tgb.text("Intended Use(s)", class_name="card-title")
        tgb.text("Because it is intended for both clinical and field applications, the proposed solution guarantees " 
        "adaptability in a range of healthcare environments. Such applications include:", class_name="card-body-text")  
        with tgb.layout("1 1"):
            with tgb.part(class_name="tech-card"):
                tgb.text("Clinical Settings", class_name="tech-title")
                tgb.text(
                    "In situations when contact-based systems are impractical, the technology will be utilized to " 
                    "continuously monitor patients' heart rates and rhythms without causing any harm. ",
                    class_name="tech-desc"
                )
            with tgb.part(class_name="tech-card"):
                tgb.text("Emergency Response", class_name="tech-title")
                tgb.text(
                    "Faster diagnosis and action are made possible by the system's instantaneous, portable cardiac " 
                    "evaluation during transportation or at the site of an accident. ",
                    class_name="tech-desc"
                )
            with tgb.part(class_name="tech-card"):
                tgb.text("Rehabilitation and Recovery", class_name="tech-title")
                tgb.text(
                    "The technology helps patients, such as those recuperating from burns or delicate disorders, who need " 
                    "regular monitoring but want a less invasive approach. ",
                    class_name="tech-desc"
                )
            with tgb.part(class_name="tech-card"):
                tgb.text("Home Healthcare", class_name="tech-title")
                tgb.text(
                    "By facilitating remote monitoring and early anomaly identification, the gadget lowers readmission rates " 
                    "to hospitals and promotes preventative treatment. ",
                    class_name="tech-desc"
                )


    #Project impact = health and safety, enviornment, sustainability, ethical
    with tgb.part(class_name="card"):
                tgb.text("Health and Safety", class_name="card-title")
                tgb.text(
                    "The main purpose of the wireless vital sign detection system is to create hardware and software to " 
                    "accurately read vital signs to avoid making contact to the intended user. This system takes into " 
                    "consideration every aspect that can be useful for contributing to the well-being of the population. " 
                    "Safety protocols and engineering processes have been considered for implementation in the proper manner. " 
                    "As well as all the constraints and risks this system may provoke in case it is not used properly or mishandled. ",
                    class_name="tech-desc"
                )
                with tgb.layout("1 1"):
                    with tgb.part(class_name="tech-card"):
                        tgb.text("Health", class_name="tech-title")
                        tgb.text(
                            "The ideal concept behind our product relies on the effectiveness of being able to improve the health of " 
                            "every individual that relies on our system. This consequently results in carefully considering each aspect " 
                            "of safety operation within the wireless vital sign detection system. That means that this development " 
                            "constantly operates at regulated radio frequencies as humans may be exposed to possible small " 
                            "radiation effects under small periods of time measuring vital signs at a proper intended " 
                            "distance from the intended user to the hardware.  ",
                            class_name="tech-desc"
                        )
                    with tgb.part(class_name="tech-card"):
                        tgb.text("Liability", class_name="tech-title")
                        tgb.text("As a set of recommendations to properly take the most advantage of our system the " 
                        "users should pay attention to these principles: ", class_name="tech-desc")
                        tgb.text("• Do not intend to modify the system in the form of damaging the circuitry or operating at a non-optimal frequency propagation. ", class_name="tech-desc")
                        tgb.text("• Keep the device away from systems that can interfere with the frequency only engineered for vital sign detection. ", class_name="tech-desc")
                        tgb.text("• Do not operate at a distance not recommended for health safety. ", class_name="tech-desc")
                        tgb.text("• Only use the device for Health applications.", class_name="tech-desc")
    with tgb.part(class_name="card"):
                tgb.text("Enviornmental", class_name="card-title")
                tgb.text(
                    "Environmental sustainability is a crucial aspect of any engineering design and considering it early in the project helps ensure that, " \
                    "throughout the life cycle of the device, none of the components or features have a negative impact on the world that surrounds us. " \
                    "Vi-Wave is designed not only to make a positive impact on the health of people, but also to promote health on the planet we " \
                    "live in by promoting the well-being of the planet through reducing unnecessary waste and incorporating environmentally conscious design choices.",
                    class_name="tech-desc"
                )
                with tgb.layout("1 1"):
                    with tgb.part(class_name="tech-card"):
                        tgb.text("Ensuring Restriction of Hazardous Substance (RoHS) compliance ", class_name="tech-title")
                        tgb.text(
                            "RoHS is a regulatory standard that originated in the European Union that bans the use of any toxic materials to be used in the " \
                            "manufacturing process of any electrical and electronic equipment. We ensure not to allow or to limit the usage of the following ten " \
                            "restricted products when developing ViWave: Cadmium, Lead, Mercury, Hexavalent Chromium, Polybrominated Biphenyls, Polybrominated Diphenyl " \
                            "Ethers, Bis(2-Ethylhexyl) phthalate, Benzyl butyl phthalate, Dibutyl phthalate, Diisobutyl phthalate.", class_name="tech-desc")
                    with tgb.part(class_name="tech-card"):
                        tgb.text("Easy and Safe Disassembly", class_name="tech-title")
                        tgb.text(
                            "Vi-Wave is a product that is easy to disassemble, as there are only a few steps in order to do so. The device consists of modular " \
                            "components that can be separated with only a few simple steps, allowing the modules to detach smoothly from one another without " \
                            "compromising the integrity of the device itself. Additionally, the device avoids usage of soldered cable connections; all required " \
                            "interfaces are handled through a standard power supply and USB links, enabling quick separation between boards and between the boards "
                            "and monitor. The antenna is detachable from the mmWaveICBOOST module as it uses a connector without any cables required. Its secure " \
                            "mechanical design keeps it firmly in place during operation, while also allowing for easy detachment or replacement without worry.",
                            class_name="tech-desc"
                        )
                    with tgb.part(class_name="tech-card"):
                        tgb.text("The Hannover Principles", class_name="tech-title")
                        tgb.text(
                            "The Hannover Principles were carefully considered and integrated throughout ViWave’s development process. The end goal is to guarantee that, " \
                            "while the project remains commercially viable, it can also coexist responsibly with the well-being of humans and environmental health. ViWave is " \
                            "promoted to humans as a device that reduces physical waste through its contactless features, ensuring coexistence between technology and environmental " \
                            "responsibility by minimizing the use of disposable sensors. Additionally, Viwave is designed as a project with distinct modules, where each component and " \
                            "module work together seamlessly without requiring destructive assembly processes. This promotes easy repairability, constant reuse, and long-term sustainability, " \
                            "acknowledging the interdependent relationship between human health, technology, and environmental impacts.",
                            class_name="tech-desc"
                        )
                    with tgb.part(class_name="tech-card"):
                        tgb.text("Life Cycle Impact Assessment (LCIA)", class_name="tech-title")
                        tgb.text(
                            "The Life Cycle Impact Assessment takes account a majority of the probable environmental effects that a project can have during its entire lifespan, " \
                            "from the early stages of development and material acquirement to the final moments of the device’s functional life. It allows us to see step by step " \
                            "how each phase either prevents environmental harm or may introduce environmental harm in order to asses which changes have to be made to reduce the overall " \
                            "environmental impact. All of this while maintaining overall functional performance. All electronic components with the modules being utilized are specified as " \
                            "RoHS compliant and avoid using lead in order to reduce the overall toxicity to humans and to stop ecological harm. In addition to its contactless capabilities, " \
                            "Vi-Wave is designed with long lasting hardware components to avoid the need for replacements. ",
                            class_name="tech-desc"
                        )
    with tgb.part(class_name="card"):
                tgb.text("Sustainability", class_name="card-title")
                tgb.text(
                    "Due to various factors our planet has fallen into a climate crisis. Countries have become overwhelmed with trash. " \
                    "Overconsumption of material goods has led to overproduction of items we do not need, most of which ends up in landfills. " \
                    "To combat this, we designed a system with sustainable practices in mind. Sustainability is the practice of development for today " \
                    "without harming the people of tomorrow.  ",
                    class_name="tech-desc"
                )
                with tgb.layout("1 1"):
                    with tgb.part(class_name="tech-card"):
                        tgb.text("Hardware", class_name="tech-title")
                        tgb.text(
                            "When it comes to hardware there are a few things that we need to consider for a sustainable design. Including, but not limited to, how to reduce resource consumption, " \
                            "extend product lifespan, be energy efficient, and use eco-friendly materials. Our hardware design aims to reduce resource consumption. " \
                            "The components utilized and our power management techniques, adopt practices that lead to reduced energy consumption and a smaller carbon footprint. " \
                            "The IWR6843 has a low power mode we will be utilizing, as well as implementing an efficient regulator, and only power external interfaces. " \
                            "In doing so we will utilize less electricity reducing our heat output. To reduce resource consumption, we will be reducing the number of discrete components " \
                            "implemented, choose recyclable components, and avoid unnecessary items, such as LEDs or connectors. ",
                            class_name="tech-desc"
                        )
                    with tgb.part(class_name="tech-card"):
                        tgb.text("Software", class_name="tech-title")
                        tgb.text(
                            "Often overlooked, but software has the potential to drastically influence hardware energy usage. All the efforts for sustainable hardware design will be wasted if " \
                            "inefficient software overloads the CPU leading to higher resource usage and energy waste. To combat this, we will use efficient algorithms, optimize radar frames, implement " \
                            "smart operations and reduce data transmission. Our goal is to lower processing load. To efficiently process radar, we will use fixed point math, and fit algorithms to " \
                            "hardware accelerators. To optimize radar frames we will lower the frame rate, reduce the number of chirps per minute and reduce ADC sampling. Active chirping " \
                            "draws the most power, so optimizing our parameters saves a lot of energy. Our software will also respond to conditions. To prevent continuous heavy processing " \
                            "the radar will sleep when no motion detected, use event driven wake up and not update the cloud when data changes. During data transmission, " \
                            "we will only send compressed data and process raw data locally. By implementing the above-mentioned practices, we ensure the CPU is not overloaded and our code uses low energy.",
                            class_name="tech-desc"
                        )
    with tgb.part(class_name="card"):
                tgb.text("Ethical Consideration and Social Impact", class_name="card-title")
                tgb.text(
                    "Our project will adhere to the IEEE Code of Ethics. If an ethical dilemma arises that does not comply with the code, we will apply the ethical theory model. The ethical " \
                    "theory model is a framework to analyze or resolve any ethical dilemmas that fall outside the scope of the Code of Ethics. ",
                    class_name="tech-desc"
                )
                with tgb.layout("1 1"):
                    with tgb.part(class_name="tech-card"):
                        tgb.text("Ethical Considerations", class_name="tech-title")
                        tgb.text(
                            "our project will adhere to the IEEE Code of Ethics. The IEEE Code of Ethics has three main points of concern, with " \
                            "multiple subpoints elaborating on said main points. First, to uphold the highest standards of integrity, responsible behavior, "
                            "and ethical behavior in professional behavior. Next, treat all persons fairly and with respect, not engaging in discrimination " \
                            "of any kind and not causing any bodily harm. Lastly, to ensure, we as Engineers uphold this code, including collaborators and co-workers. ",
                            class_name="tech-desc"
                        )
                    with tgb.part(class_name="tech-card"):
                        tgb.text("Social Impact", class_name="tech-title")
                        tgb.text(
                            "Our intention is to bring convenience and comfort to individuals. Traditional vital sign detection systems require physical contact with patients to " \
                            "capture data. But what about individuals on the spectrum who have sensory issues? What about burn victims? There are many groups of people how might " \
                            "not be comfortable or able to capture vital signs in the traditional way. Not only will we bring convenience, but our product can be used in emergency situations. " \
                            "We reside in South Florida, which is impacted by hurricanes for much of the year. With heavy rain and destructive winds, the aftermath of many hurricanes " \
                            "leaves Floridians with destructed homes and missing or hurt individuals. Our system would allow first responders to take vitals of patients they might not be able to reach. " \
                            "This can be scaled to a global level as well. During tense situations such as war or natural disasters, our system will provide easier aid to affected individuals. " \
                            "Not only will we provide comfort, but the device also reduces the risk of cross-contamination and enhances accessibility.  ",
                            class_name="tech-desc"
                        )


    #Meet the Team
    with tgb.part(class_name="card"):
        tgb.text("Meet the Team", class_name="card-title")
        tgb.text(
            "Our project combines software and hardware, specifically power, electronics, "
            "and radio frequency. Due to the different features of our design, it is essential " \
            "to form a team with multidisciplinary skills.",
            class_name="card-body-text"
        )
        with tgb.layout("1 1 1"):
            with tgb.part(class_name="team-card"):
                tgb.text("Marcos Bucarito", class_name="team-name")
                tgb.text("Oversees the integration of the radar and RF subsystems", class_name="team-role")
                tgb.text("Electrical engineering major with experience in research and competition. " 
                "Through his research at Florida International University, he brings knowledge of " 
                "radio frequency electronic design, as well as networking expertise gained from his " 
                "IT consulting work. In turn, his skill set ensures a robust, calibrated, and " 
                "optimized wireless front end and communication path.", class_name="team-desc")
            with tgb.part(class_name="team-card"):
                tgb.text("Diego Santaella", class_name="team-name")
                tgb.text("Oversees PCB and embedded design", class_name="team-role")
                tgb.text("Electrical engineering major with extensive technical experience through " 
                "internships. Santaella applies his PCB design experience and embedded hardware background " 
                "to integrate sensors, electronics, and interfaces. Promising a reliable, testable system, " 
                "which he can effectively troubleshoot. In addition to having foundational " 
                "knowledge of radio frequency.", class_name="team-desc")
            with tgb.part(class_name="team-card"):
                tgb.text("Kendly Jean", class_name="team-name")
                tgb.text("Oversees hardware debugging and test automation", class_name="team-role")
                tgb.text("Electrical engineer bringing in technical experience through internships. " 
                "Jean brings experience in PCB design, programming skills, and exposure to debugging "
                "and troubleshooting boards. Through previous experience, he has automated test solutions "
                "and board bring-up in addition to enrolling in a communications systems course to learn " 
                "more about radio frequency principles.", class_name="team-desc")
        with tgb.layout("1 1"):
            with tgb.part(class_name="team-card"):
                tgb.text("Maria Abrahamyan", class_name="team-name")
                tgb.text("Oversees software development and signal processing", class_name="team-role")
                tgb.text("Computer engineering major with experience in medical research and technical skills" 
                         "gained through internship work. Bringing in experience with C++, C#, and Java, as " 
                         "well as designing low-level systems for data processing, implementing machine learning " 
                         "models, and developing software for embedded systems, and aiding in extracting " 
                         "meaningful health metrics from raw radio frequency data.", class_name="team-desc")
            with tgb.part(class_name="team-card"):
                tgb.text("Juan Niebla", class_name="team-name")
                tgb.text("Oversees power management and safety testing", class_name="team-role")
                tgb.text("Electrical engineering major with experience in energy research, power design, and " 
                "electrical work. Niebla ensures that the system is power-efficient and thoroughly tested. " 
                "Applying his hardware and power systems knowledge to guarantee safe and reliable operation. ", class_name="team-desc")

    #Acknowledgements
    with tgb.part(class_name="card"):
        tgb.text("Acknowledgements", class_name="card-title")
        tgb.text(
            "The team would like to acknowledge the contributions of the following individuals who made this research-based project possible through their efforts.  " 
            "We extend our gratitude to Florida International University for providing the funding and resources necessary to support the development of our project. " 
            "This provided us with an opportunity to explore additional approaches to achieving higher accuracy in our Vi-Wave project by utilizing mmWave Radar technology.  " 
            "We acknowledge the team members of our project and others who collectively contributed, demonstrating commitment and investing time to develop " 
            "innovative solutions for this project. We would like to extend our gratitude to Michael McChesney, a PhD student who contributed his time and technical " 
            "guidance to aid in our understanding of how Radio Frequency and Radar Systems Technology works.  " 
            "Another notable mention is Professor Konstantinos Zekios, our mentor, who helped steer us in the right direction and provided valuable advice on how " 
            "to approach and solve the problem. His insights guided us through complex concepts and approaches to radio frequency systems, refining our ideas and expertise.  " 
            "This research-based project would not have been possible without the contributions of effort, knowledge, commitment, and collaborative " 
            "working relationships among the team members involved. ",
            class_name="card-body-text"
        )

    # Contact
    with tgb.part(class_name="card"):
        tgb.text("Contact", class_name="card-title")
        tgb.text("For inquiries about the VI-Wave project, please reach out:", class_name="card-body-text")
        tgb.text("Email: VI.Waveinc@gmail.com", class_name="contact-info")
        tgb.text("Institution: Florida International University, Department of Electrical and Computer Engineering", class_name="contact-info")
        tgb.text("Project Year: 2025 – 2026", class_name="contact-info")

    with tgb.part(class_name="disclaimer-bar"):
        tgb.text(
            "This tool is for informational purposes only and not medical advice.",
            class_name="disclaimer-text"
        )