import streamlit as st
import pandas as pd

# ======== DATA STRUCTURES ========
# At the top of your app.py file
from supplement_data import get_supplement_data, get_interactions_data, get_age_health_concerns

# Then replace your load_data function with this:
def load_data():
    """Load supplement data from the separate module"""
    supplements_data = get_supplement_data()
    interactions_data = get_interactions_data()
    age_health_concerns = get_age_health_concerns()
    
    return supplements_data, interactions_data, age_health_concerns
    
    # Interactions data
    interactions_data = {
        "calcium": ["iron", "zinc", "magnesium"],
        "iron": ["calcium", "vitamin_e", "zinc"],
        "zinc": ["calcium", "iron", "copper"],
        "magnesium": ["calcium"],
        "vitamin_c": ["b12"],
        "vitamin_e": ["vitamin_k2"]
    }
    
    # Health concerns by age group and gender
    age_health_concerns = {
        "20s": {
            "male": ["immune_support", "fitness_performance", "stress"],
            "female": ["immune_support", "iron_deficiency", "stress", "reproductive_health"],
            "prefer_not_to_say": ["immune_support", "stress", "fitness_performance"]
        },
        "30s": {
            "male": ["energy_levels", "stress", "immune_support", "fitness_performance"],
            "female": ["energy_levels", "stress", "reproductive_health", "iron_deficiency"],
            "prefer_not_to_say": ["energy_levels", "stress", "immune_support"]
        },
        "40s": {
            "male": ["heart_health", "energy_levels", "stress", "longevity"],
            "female": ["energy_levels", "stress", "bone_health", "hormone_balance"],
            "prefer_not_to_say": ["energy_levels", "stress", "heart_health", "longevity"]
        },
        "50s": {
            "male": ["heart_health", "prostate_health", "joint_pain", "cognitive_function", "longevity"],
            "female": ["bone_health", "hormone_balance", "heart_health", "joint_pain", "longevity"],
            "prefer_not_to_say": ["heart_health", "joint_pain", "cognitive_function", "longevity"]
        },
        "60s": {
            "male": ["heart_health", "joint_pain", "cognitive_function", "prostate_health", "longevity"],
            "female": ["bone_health", "heart_health", "joint_pain", "cognitive_function", "longevity"],
            "prefer_not_to_say": ["heart_health", "joint_pain", "cognitive_function", "longevity"]
        },
        "70plus": {
            "male": ["heart_health", "cognitive_function", "bone_health", "immune_support", "longevity"],
            "female": ["bone_health", "heart_health", "cognitive_function", "immune_support", "longevity"],
            "prefer_not_to_say": ["heart_health", "cognitive_function", "bone_health", "immune_support", "longevity"]
        }
    }
    
    return supplements_data, interactions_data, age_health_concerns

# ======== UI FUNCTIONS ========

def display_header():
    st.title("Personalized Vitamin & Supplement Advisor")
    st.markdown("""
    This application provides personalized supplement recommendations based on your age, gender, and health concerns.
    Recommendations include potential interactions and are organized by budget tier with sourced information.
    
    **Disclaimer:** This tool provides general information only and is not a substitute for professional medical advice.
    Always consult with a healthcare provider before starting any supplement regimen.
    """)

def get_user_info():
    col1, col2 = st.columns(2)
    
    with col1:
        age_group = st.selectbox(
            "Select your age group:",
            ["20s", "30s", "40s", "50s", "60s", "70plus"]
        )
        
    with col2:
        gender = st.selectbox(
            "Select your gender:",
            ["female", "male", "prefer_not_to_say"]
        )
    
    return age_group, gender

def get_health_concerns(all_supplements, age_health_concerns, age_group, gender):
    # Extract all possible health concerns from the supplement data
    all_health_concerns = set()
    for supplement in all_supplements.values():
        for concern in supplement["recommended_for"]["health_concerns"]:
            all_health_concerns.add(concern)
    
    # Convert to list and sort alphabetically
    all_health_concerns = sorted(list(all_health_concerns))
    
    # Get recommended concerns for this age group and gender
    recommended_concerns = age_health_concerns.get(age_group, {}).get(gender, [])
    
    # Create a readable mapping for display
    concern_mapping = {
        "bone_health": "Bone Health",
        "immune_support": "Immune System Support",
        "depression": "Mood Support/Depression",
        "muscle_cramps": "Muscle Cramps",
        "sleep_issues": "Sleep Issues",
        "stress": "Stress Management",
        "heart_health": "Heart Health",
        "joint_pain": "Joint Pain",
        "cognitive_function": "Cognitive Function/Brain Health",
        "fatigue": "Fatigue/Energy Levels",
        "vegetarian_vegan": "Vegetarian/Vegan Diet",
        "anemia": "Anemia/Low Iron",
        "digestive_issues": "Digestive Issues",
        "antibiotic_recovery": "Recovery from Antibiotics",
        "skin_health": "Skin Health",
        "iron_deficiency": "Iron Deficiency",
        "heavy_periods": "Heavy Menstrual Periods",
        "osteoporosis_risk": "Osteoporosis Risk",
        "fitness_performance": "Fitness Performance",
        "reproductive_health": "Reproductive Health",
        "hormone_balance": "Hormone Balance",
        "prostate_health": "Prostate Health",
        "statin_users": "Taking Statin Medications",
        "respiratory_issues": "Respiratory Issues",
        "liver_health": "Liver Health",
        "longevity": "Longevity/Anti-Aging",
        "eye_health": "Eye Health",
        "nerve_health": "Nerve Health",
        "adrenal_support": "Adrenal Support",
        "detoxification_support": "Detoxification Support",
        "hair_health": "Hair Health",
        "nail_health": "Nail Health",
        "wound_healing": "Wound Healing",
        "muscle_loss_prevention": "Muscle Loss Prevention",
        "antibiotic_recovery": "Recovery from Antibiotics",
        "blood_pressure": "Blood Pressure Management",
        "menopause_symptoms": "Menopause Symptoms",
        "circulation": "Circulation",
        "tinnitus": "Tinnitus",
        "migraine_prevention": "Migraine Prevention",
        "memory_support": "Memory Support",
        "weight_management": "Weight Management",
        "exercise_recovery": "Exercise Recovery",
        "allergies": "Allergies",
        "jet_lag": "Jet Lag",
        "shift_work": "Shift Work Support",
        "herpes_management": "Herpes Management",
        "cholesterol_management": "Cholesterol Management",
        "pms_symptoms": "PMS Symptoms",
        "mood_support": "Mood Support"

    }
    
    # Convert technical terms to readable format for display
    display_concerns = {concern: concern_mapping.get(concern, concern.replace("_", " ").title()) 
                       for concern in all_health_concerns}
    
    # Create two columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Common Health Concerns")
        # Show recommended concerns first with pre-selected checkboxes
        selected_concerns = []
        for concern in recommended_concerns:
            if concern in display_concerns:
                label = display_concerns[concern]
                if st.checkbox(label, value=False, key=f"rec_{concern}"):
                    selected_concerns.append(concern)
    
    with col2:
        st.subheader("Additional Health Concerns")
        # Show other concerns
        other_concerns = [c for c in all_health_concerns if c not in recommended_concerns]
        for concern in other_concerns:
            label = display_concerns[concern]
            if st.checkbox(label, value=False, key=f"other_{concern}"):
                selected_concerns.append(concern)
                
    # Input for medications
    st.subheader("Current Medications")
    medications = st.text_input("List any medications you are currently taking (separated by commas):")
    
    return selected_concerns, medications

def select_budget_tier():
    st.subheader("Budget Preference")
    tier = st.radio(
        "Select your budget tier:",
        ["essential", "good", "ideal"],
        index=1,  # Default to "good"
        format_func=lambda x: {
            "essential": "Essential (Most affordable options)",
            "good": "Good (Balanced quality and cost)",
            "ideal": "Ideal (Premium quality options)"
        }.get(x)
    )
    return tier

def get_recommended_supplements(supplements_data, age_group, gender, health_concerns):
    recommended = {}
    
    for supp_id, supplement in supplements_data.items():
        # Check if supplement is recommended for this age group and gender
        if (age_group in supplement["recommended_for"]["age_groups"] and
            gender in supplement["recommended_for"]["genders"]):
            
            # Check if any health concerns match
            matching_concerns = [concern for concern in health_concerns 
                                if concern in supplement["recommended_for"]["health_concerns"]]
            
            if matching_concerns:
                # Calculate a relevance score based on how many concerns match
                relevance = len(matching_concerns) / len(health_concerns) if health_concerns else 0
                recommended[supp_id] = {
                    "supplement": supplement,
                    "matching_concerns": matching_concerns,
                    "relevance": relevance
                }
    
    # Sort by relevance score
    sorted_recommendations = dict(sorted(recommended.items(), 
                                 key=lambda x: x[1]["relevance"], 
                                 reverse=True))
    
    return sorted_recommendations

def check_interactions(recommendations, interactions_data, medications):
    """Check for potential interactions between recommended supplements and with medications."""
    
    potential_interactions = {}
    
    # Check supplement-to-supplement interactions
    supplement_ids = list(recommendations.keys())
    
    for i, supp_id in enumerate(supplement_ids):
        interactions = []
        
        # Check against interactions data
        if supp_id in interactions_data:
            for interacting_supp in interactions_data[supp_id]:
                if interacting_supp in supplement_ids:
                    interactions.append({
                        "type": "supplement",
                        "name": recommendations[interacting_supp]["supplement"]["name"],
                        "note": "May reduce absorption when taken together. Take at least 2 hours apart."
                    })
        
        # Check against medication interactions
        if medications:
            med_list = [med.strip().lower() for med in medications.split(",")]
            supp_data = recommendations[supp_id]["supplement"]
            
            for med in med_list:
                for interaction in supp_data.get("interactions", []):
                    # Simple keyword matching (in a real app, would use a more sophisticated approach)
                    if med in interaction or interaction in med:
                        interactions.append({
                            "type": "medication",
                            "name": med,
                            "note": f"Potential interaction with {med}. Consult healthcare provider."
                        })
        
        if interactions:
            potential_interactions[supp_id] = interactions
    
    return potential_interactions

def display_recommendations(recommendations, interactions, budget_tier, age_group):
    st.header("Your Personalized Supplement Recommendations")
    
    if not recommendations:
        st.warning("No specific supplements recommended based on your selections.")
        return
    
    # Tier explanation
    tier_descriptions = {
        "essential": "These are the most affordable options that provide basic nutritional support.",
        "good": "These options balance quality and cost, often with improved forms and absorption.",
        "ideal": "These premium options typically offer the most bioavailable forms and additional supporting nutrients."
    }
    
    st.markdown(f"**{budget_tier.title()} Tier**: {tier_descriptions[budget_tier]}")
    
    # Create expandable sections for each recommendation
    for supp_id, rec_data in recommendations.items():
        supplement = rec_data["supplement"]
        matching_concerns = rec_data["matching_concerns"]
        
        # Format concerns for display
        concern_display = [c.replace("_", " ").title() for c in matching_concerns]
        
        with st.expander(f"**{supplement['name']}**"):
            # Main information
            st.markdown(f"**Benefits**: {supplement['benefits']}")
            st.markdown(f"**Recommended for**: {', '.join(concern_display)}")
            st.markdown(f"**Suggested dosage**: {supplement['dosage'].get(age_group, 'Not specified')}")
            
            # Budget tier information
            tier_info = supplement["budget_tier"][budget_tier]
            st.markdown(f"**Recommended form**: {tier_info['form']}")
            st.markdown(f"**Typical price range**: {tier_info['price_range']}")
            if "note" in tier_info:
                st.markdown(f"**Note**: {tier_info['note']}")
            
            # Interaction warnings
            if supp_id in interactions:
                st.markdown("### ⚠️ Potential Interactions")
                for interaction in interactions[supp_id]:
                    st.markdown(f"- **{interaction['name']}**: {interaction['note']}")
            
            # Contraindications
            if supplement.get("contraindications"):
                contraindications = [c.replace("_", " ").title() for c in supplement.get("contraindications", [])]
                st.markdown(f"**Use caution if you have**: {', '.join(contraindications)}")
            
            # Sources
            st.markdown("### Sources")
            for source in supplement.get("sources", []):
                st.markdown(f"- [{source}]({source})")

def display_timing_guide(recommendations):
    st.header("Supplement Timing Guide")
    
    if not recommendations:
        return
    
    # Create general timing categories
    timing_categories = {
        "morning_with_food": [],
        "morning_empty_stomach": [],
        "afternoon": [],
        "evening_with_food": [],
        "evening_empty_stomach": [],
        "bedtime": []
    }
    
    # Simple rules for categorizing supplements
    for supp_id, rec_data in recommendations.items():
        supplement = rec_data["supplement"]
        name = supplement["name"]
        
        if name in ["Iron"]:
            timing_categories["morning_empty_stomach"].append(name)
        elif name in ["Vitamin D", "Vitamin B12", "Omega-3 Fatty Acids"]:
            timing_categories["morning_with_food"].append(name)
        elif name in ["Probiotics"]:
            timing_categories["morning_empty_stomach"].append(name)
        elif name in ["Vitamin C", "Choline", "Taurine"]:
            timing_categories["afternoon"].append(name)
        elif name in ["Calcium"]:
            timing_categories["evening_with_food"].append(name)
        elif name in ["Magnesium"]:
            timing_categories["bedtime"].append(name)
        else:
            # Default to morning with food if no specific rule
            timing_categories["morning_with_food"].append(name)
    
    # Display timing recommendations
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Morning")
        if timing_categories["morning_empty_stomach"]:
            st.markdown("**On empty stomach:**")
            for supp in timing_categories["morning_empty_stomach"]:
                st.markdown(f"- {supp}")
        
        if timing_categories["morning_with_food"]:
            st.markdown("**With breakfast:**")
            for supp in timing_categories["morning_with_food"]:
                st.markdown(f"- {supp}")
        
        st.subheader("Afternoon")
        if timing_categories["afternoon"]:
            for supp in timing_categories["afternoon"]:
                st.markdown(f"- {supp}")
    
    with col2:
        st.subheader("Evening")
        if timing_categories["evening_with_food"]:
            st.markdown("**With dinner:**")
            for supp in timing_categories["evening_with_food"]:
                st.markdown(f"- {supp}")
        
        if timing_categories["evening_empty_stomach"]:
            st.markdown("**After dinner (2+ hours):**")
            for supp in timing_categories["evening_empty_stomach"]:
                st.markdown(f"- {supp}")
        
        st.subheader("Bedtime")
        if timing_categories["bedtime"]:
            for supp in timing_categories["bedtime"]:
                st.markdown(f"- {supp}")
    
    # General timing advice
    st.markdown("""
    ### General Timing Tips:
    1. **Fat-soluble vitamins** (A, D, E, K) are best absorbed with fatty meals
    2. **Iron** absorbs better on an empty stomach, but can cause stomach upset (take with vitamin C to enhance absorption)
    3. **B vitamins** may boost energy, so taking them late in the day might affect sleep
    4. **Calcium and magnesium** can compete for absorption, so take at different times
    5. **Probiotics** are often best taken in the morning on an empty stomach
    """)

def create_supplement_plan(recommendations, budget_tier, interactions, age_group):
    st.header("Your Personalized Supplement Plan")
    
    if not recommendations:
        st.warning("No specific supplements recommended based on your selections.")
        return
    
    # Create formatted plan
    plan_text = "# Your Personalized Supplement Plan\n\n"
    plan_text += f"## {budget_tier.title()} Tier Recommendations\n\n"
    
    for supp_id, rec_data in recommendations.items():
        supplement = rec_data["supplement"]
        tier_info = supplement["budget_tier"][budget_tier]
        
        plan_text += f"### {supplement['name']}\n"
        plan_text += f"- **Form:** {tier_info['form']}\n"
        plan_text += f"- **Dosage:** {supplement['dosage'].get(age_group, 'Consult healthcare provider')}\n"
        plan_text += f"- **Typical Price:** {tier_info['price_range']}\n"
        
        if supp_id in interactions and interactions[supp_id]:
            plan_text += "- **Special Considerations:**\n"
            for interaction in interactions[supp_id]:
                plan_text += f"  - *{interaction['name']}*: {interaction['note']}\n"
        
        plan_text += "\n"
    
    # Add general advice
    plan_text += """## General Recommendations

1. **Start gradually**: Introduce one supplement at a time to monitor for any adverse reactions.
2. **Consistency matters**: Take supplements consistently at the same time(s) each day.
3. **Follow timing guidelines**: Some supplements are better absorbed at specific times or with/without food.
4. **Regular reassessment**: Reassess your supplement needs every 6-12 months or with any significant health changes.
5. **Quality matters**: Look for supplements that have been third-party tested (USP, NSF, or ConsumerLab verification).

## Important Disclaimer
This supplement plan is provided for informational purposes only and is not a substitute for professional medical advice. Always consult with a healthcare provider before starting any supplement regimen, especially if you have health conditions or take medications.
"""
    
    # Display the plan and offer download
    st.markdown(plan_text)
    
    # In a real app, you would generate a PDF here
    st.download_button(
        label="Download Supplement Plan (PDF)",
        data=plan_text,
        file_name="personalized_supplement_plan.txt",
        mime="text/plain"
    )

# ======== MAIN APPLICATION ========

def main():
    # Load data
    supplements_data, interactions_data, age_health_concerns = load_data()
    
    # Display header and get user information
    display_header()
    age_group, gender = get_user_info()
    
    # Get health concerns based on age and gender
    health_concerns, medications = get_health_concerns(supplements_data, age_health_concerns, age_group, gender)
    
    # Select budget tier
    budget_tier = select_budget_tier()
    
    # Generate recommendations button
    if st.button("Generate Recommendations"):
        if not health_concerns:
            st.warning("Please select at least one health concern for personalized recommendations.")
        else:
            # Get recommendations based on user input
            recommendations = get_recommended_supplements(supplements_data, age_group, gender, health_concerns)
            
            # Check for potential interactions
            interactions = check_interactions(recommendations, interactions_data, medications)
            
            # Display recommendations - Now passing age_group as parameter
            display_recommendations(recommendations, interactions, budget_tier, age_group)
            
            # Display timing guide
            display_timing_guide(recommendations)
            
            # Create and offer downloadable plan - Now passing age_group as parameter
            create_supplement_plan(recommendations, budget_tier, interactions, age_group)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    **Disclaimer:** This application provides general information and is not a substitute for professional medical advice. 
    All recommendations should be reviewed with a healthcare provider before implementation.
    """)

if __name__ == "__main__":
    main()
