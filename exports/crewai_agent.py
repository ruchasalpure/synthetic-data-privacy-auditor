from crewai import Agent

synthetic_data_privacy_auditor = Agent(
    role="Synthetic Data Privacy Auditor",
    goal="Deliver high-precision autonomous Synthetic Data Privacy Auditor operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
