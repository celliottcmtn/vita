import streamlit as st
import pandas as pd

# ======== DATA STRUCTURES ========

# Load data from JSON files (in a real app, we would have these data files)
def load_data():
    """
    Load supplement data from JSON files.
    In a production environment, these would be actual files.
    """
    # Sample data structure - in production, load from files
    supplements_data = {
        "vitamin_d": {
            "name": "Vitamin D",
            "benefits": "Bone health, immune function, mood regulation",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["bone_health", "immune_support", "depression", "longevity"]
            },
            "dosage": {
                "20s": "1000-2000 IU daily",
                "30s": "1000-2000 IU daily",
                "40s": "1000-2000 IU daily",
                "50s": "1000-4000 IU daily",
                "60s": "1000-4000 IU daily",
                "70plus": "2000-4000 IU daily"
            },
            "contraindications": ["hypercalcemia", "kidney_disease"],
            "interactions": ["steroids", "weight_loss_drugs", "cholesterol_medication"],
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminD-HealthProfessional/"],
            "budget_tier": {
                "essential": {
                    "form": "D3 tablets",
                    "price_range": "$5-15 for 3-month supply"
                },
                "good": {
                    "form": "Mixed carotenoids with preformed vitamin A",
                    "price_range": "$10-20 for 3-month supply"
                },
                "ideal": {
                    "form": "Full-spectrum vitamin A complex with fat-soluble cofactors",
                    "price_range": "$20-35 for 3-month supply"
                }
            }
        },
        "quercetin": {
            "name": "Quercetin",
            "benefits": "Anti-inflammatory, antioxidant, immune support, anti-allergy",
            "recommended_for": {
                "age_groups": ["30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["immune_support", "allergies", "inflammation", "longevity"]
            },
            "dosage": {
                "30s": "500-1000 mg daily",
                "40s": "500-1000 mg daily",
                "50s": "500-1000 mg daily",
                "60s": "500-1000 mg daily",
                "70plus": "500-1000 mg daily"
            },
            "contraindications": [],
            "interactions": ["blood_thinners", "antibiotics", "cyclosporine"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5214562/"],
            "budget_tier": {
                "essential": {
                    "form": "Quercetin dihydrate",
                    "price_range": "$15-25 for 1-month supply"
                },
                "good": {
                    "form": "Quercetin with bromelain",
                    "price_range": "$25-40 for 1-month supply"
                },
                "ideal": {
                    "form": "Quercetin phytosome or liposomal formula",
                    "price_range": "$40-60 for 1-month supply"
                }
            }
        },
        "berberine": {
            "name": "Berberine",
            "benefits": "Blood sugar control, cholesterol management, gut health",
            "recommended_for": {
                "age_groups": ["40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["blood_sugar_management", "heart_health", "digestive_issues", "longevity"]
            },
            "dosage": {
                "40s": "500-1500 mg daily (divided doses)",
                "50s": "500-1500 mg daily (divided doses)",
                "60s": "500-1500 mg daily (divided doses)",
                "70plus": "500-1500 mg daily (divided doses)"
            },
            "contraindications": ["pregnancy", "jaundice"],
            "interactions": ["diabetes_medications", "blood_thinners", "certain_antibiotics"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6111450/"],
            "budget_tier": {
                "essential": {
                    "form": "Berberine HCl",
                    "price_range": "$20-30 for 1-month supply"
                },
                "good": {
                    "form": "Berberine complex with alpha-lipoic acid",
                    "price_range": "$30-45 for 1-month supply"
                },
                "ideal": {
                    "form": "Dihydroberberine or high-absorption berberine",
                    "price_range": "$45-70 for 1-month supply"
                }
            }
        }
    }
    
    # Interactions data - which supplements may reduce efficacy when taken together
    interactions_data = {
        "calcium": ["iron", "zinc", "magnesium"],
        "iron": ["calcium", "vitamin_e", "zinc"],
        "zinc": ["calcium", "iron", "copper"],
        "magnesium": ["calcium"],
        "vitamin_c": ["b12"],
        "vitamin_e": ["vitamin_k2"],
        "curcumin": ["iron"],
        "quercetin": ["iron"],
        "vitamin_a": ["vitamin_e", "vitamin_k2"]
    }
    
    # Health concerns that are more common or important by age group and gender
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
        "blood_sugar_management": "Blood Sugar Management",
        "allergies": "Allergies",
        "inflammation": "Inflammation",
        "eye_health": "Eye Health",
        "muscle_loss_prevention": "Muscle Loss Prevention"
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
        elif name in ["Vitamin D", "Vitamin B12", "Omega-3 Fatty Acids", "Coenzyme Q10 (CoQ10)", "Vitamin A", "Vitamin E"]:
            timing_categories["morning_with_food"].append(name)
        elif name in ["Probiotics"]:
            timing_categories["morning_empty_stomach"].append(name)
        elif name in ["Vitamin C", "Choline", "Taurine", "Berberine"]:
            timing_categories["afternoon"].append(name)
        elif name in ["Calcium", "Curcumin (Turmeric Extract)"]:
            timing_categories["evening_with_food"].append(name)
        elif name in ["Magnesium", "Ashwagandha"]:
            timing_categories["bedtime"].append(name)
        elif name in ["Vitamin K2", "Zinc", "Quercetin", "Creatine"]:
            timing_categories["morning_with_food"].append(name)
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
    6. **Adaptogens** like Ashwagandha may support sleep when taken in the evening
    7. **Berberine** should be taken before meals for blood sugar support
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
    "form": "D3 + K2 combination",
                    "price_range": "$15-25 for 3-month supply"
                },
                "ideal": {
                    "form": "Liposomal D3 + K2 with organic oils",
                    "price_range": "$25-40 for 3-month supply"
                }
            }
        },
        "magnesium": {
            "name": "Magnesium",
            "benefits": "Muscle function, nerve function, energy production, sleep quality",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["muscle_cramps", "sleep_issues", "stress", "heart_health", "longevity"]
            },
            "dosage": {
                "20s": "310-400 mg daily",
                "30s": "310-420 mg daily",
                "40s": "320-420 mg daily",
                "50s": "320-420 mg daily",
                "60s": "320-420 mg daily",
                "70plus": "320-420 mg daily"
            },
            "contraindications": ["kidney_failure"],
            "interactions": ["antibiotics", "diuretics", "heart_medication"],
            "sources": ["https://ods.od.nih.gov/factsheets/Magnesium-HealthProfessional/"],
            "budget_tier": {
                "essential": {
                    "form": "Magnesium oxide",
                    "price_range": "$5-10 for 2-month supply",
                    "note": "Less bioavailable but affordable"
                },
                "good": {
                    "form": "Magnesium citrate or glycinate",
                    "price_range": "$15-25 for 2-month supply"
                },
                "ideal": {
                    "form": "Magnesium threonate or glycinate complex with B6",
                    "price_range": "$30-45 for 2-month supply"
                }
            }
        },
        "omega_3": {
            "name": "Omega-3 Fatty Acids",
            "benefits": "Heart health, brain function, anti-inflammatory, joint support",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["heart_health", "joint_pain", "cognitive_function", "depression", "longevity"]
            },
            "dosage": {
                "20s": "1000-2000 mg daily",
                "30s": "1000-2000 mg daily",
                "40s": "1000-3000 mg daily",
                "50s": "1000-3000 mg daily",
                "60s": "1000-3000 mg daily",
                "70plus": "1000-3000 mg daily"
            },
            "contraindications": ["bleeding_disorders"],
            "interactions": ["blood_thinners", "high_blood_pressure_medication"],
            "sources": ["https://ods.od.nih.gov/factsheets/Omega3FattyAcids-HealthProfessional/"],
            "budget_tier": {
                "essential": {
                    "form": "Fish oil capsules",
                    "price_range": "$10-20 for 2-month supply"
                },
                "good": {
                    "form": "Concentrated fish oil (higher EPA/DHA)",
                    "price_range": "$20-35 for 2-month supply"
                },
                "ideal": {
                    "form": "Triglyceride-form fish oil or algae-based (vegetarian)",
                    "price_range": "$35-60 for 2-month supply"
                }
            }
        },
        "vitamin_b12": {
            "name": "Vitamin B12",
            "benefits": "Nerve function, red blood cell formation, DNA synthesis, energy metabolism",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["fatigue", "vegetarian_vegan", "anemia", "cognitive_function"]
            },
            "dosage": {
                "20s": "2.4 mcg daily",
                "30s": "2.4 mcg daily",
                "40s": "2.4 mcg daily",
                "50s": "2.4 mcg daily",
                "60s": "2.4-1000 mcg daily",
                "70plus": "2.4-1000 mcg daily (higher doses for absorption issues)"
            },
            "contraindications": [],
            "interactions": ["metformin", "acid_reducers"],
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminB12-HealthProfessional/"],
            "budget_tier": {
                "essential": {
                    "form": "Cyanocobalamin tablets/capsules",
                    "price_range": "$5-10 for 4-month supply"
                },
                "good": {
                    "form": "Methylcobalamin tablets",
                    "price_range": "$10-20 for 3-month supply"
                },
                "ideal": {
                    "form": "Sublingual methylcobalamin with intrinsic factor",
                    "price_range": "$20-35 for 3-month supply"
                }
            }
        },
        "probiotics": {
            "name": "Probiotics",
            "benefits": "Gut health, immune function, digestion support",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["digestive_issues", "antibiotic_recovery", "immune_support", "longevity"]
            },
            "dosage": {
                "20s": "10-30 billion CFU daily",
                "30s": "10-30 billion CFU daily",
                "40s": "10-30 billion CFU daily",
                "50s": "10-30 billion CFU daily",
                "60s": "10-30 billion CFU daily",
                "70plus": "10-30 billion CFU daily"
            },
            "contraindications": ["severe_immunodeficiency"],
            "interactions": ["antibiotics"],
            "sources": ["https://www.nccih.nih.gov/health/probiotics-what-you-need-to-know"],
            "budget_tier": {
                "essential": {
                    "form": "Single-strain probiotics",
                    "price_range": "$10-15 for 1-month supply"
                },
                "good": {
                    "form": "Multi-strain probiotics (5-10 strains)",
                    "price_range": "$20-30 for 1-month supply"
                },
                "ideal": {
                    "form": "Shelf-stable multi-strain (10+ strains) with prebiotic",
                    "price_range": "$35-50 for 1-month supply"
                }
            }
        },
        "vitamin_c": {
            "name": "Vitamin C",
            "benefits": "Immune support, antioxidant, collagen production, iron absorption",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["immune_support", "skin_health", "iron_deficiency", "longevity"]
            },
            "dosage": {
                "20s": "75-90 mg daily",
                "30s": "75-90 mg daily",
                "40s": "75-90 mg daily",
                "50s": "75-90 mg daily",
                "60s": "75-90 mg daily",
                "70plus": "75-90 mg daily (up to 500-1000 mg for immune support)"
            },
            "contraindications": ["history_of_kidney_stones"],
            "interactions": ["blood_thinners", "statins", "chemotherapy"],
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminC-HealthProfessional/"],
            "budget_tier": {
                "essential": {
                    "form": "Ascorbic acid tablets",
                    "price_range": "$5-10 for 3-month supply"
                },
                "good": {
                    "form": "Buffered vitamin C with bioflavonoids",
                    "price_range": "$15-25 for 3-month supply"
                },
                "ideal": {
                    "form": "Liposomal vitamin C or whole-food vitamin C complex",
                    "price_range": "$25-45 for 2-month supply"
                }
            }
        },
        "iron": {
            "name": "Iron",
            "benefits": "Red blood cell formation, oxygen transport, energy metabolism",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s"],
                "genders": ["female", "prefer_not_to_say"],  # More common for females but can apply to anyone
                "health_concerns": ["anemia", "fatigue", "heavy_periods", "vegetarian_vegan"]
            },
            "dosage": {
                "20s": "18 mg daily (menstruating females), 8 mg daily (others)",
                "30s": "18 mg daily (menstruating females), 8 mg daily (others)",
                "40s": "18 mg daily (menstruating females), 8 mg daily (others)",
                "50s": "8-18 mg daily (depends on menopause status)"
            },
            "contraindications": ["hemochromatosis", "thalassemia"],
            "interactions": ["calcium_supplements", "antacids", "certain_antibiotics", "vitamin_e"],
            "sources": ["https://ods.od.nih.gov/factsheets/Iron-HealthProfessional/"],
            "budget_tier": {
                "essential": {
                    "form": "Ferrous sulfate",
                    "price_range": "$5-10 for 3-month supply"
                },
                "good": {
                    "form": "Ferrous gluconate or ferrous glycinate",
                    "price_range": "$10-20 for 3-month supply"
                },
                "ideal": {
                    "form": "Iron bisglycinate chelate with vitamin C",
                    "price_range": "$20-35 for 3-month supply"
                }
            }
        },
        "calcium": {
            "name": "Calcium",
            "benefits": "Bone health, muscle function, nerve transmission",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["female", "prefer_not_to_say"],  # Especially important for women, but can apply to anyone
                "health_concerns": ["bone_health", "osteoporosis_risk"]
            },
            "dosage": {
                "20s": "1000 mg daily",
                "30s": "1000 mg daily",
                "40s": "1000 mg daily",
                "50s": "1200 mg daily",
                "60s": "1200 mg daily",
                "70plus": "1200 mg daily"
            },
            "contraindications": ["hypercalcemia", "kidney_stones"],
            "interactions": ["iron_supplements", "thyroid_medication", "certain_antibiotics", "zinc"],
            "sources": ["https://ods.od.nih.gov/factsheets/Calcium-HealthProfessional/"],
            "budget_tier": {
                "essential": {
                    "form": "Calcium carbonate",
                    "price_range": "$5-10 for 2-month supply"
                },
                "good": {
                    "form": "Calcium citrate",
                    "price_range": "$15-25 for 2-month supply"
                },
                "ideal": {
                    "form": "Calcium citrate with vitamin D3, K2, and magnesium",
                    "price_range": "$25-40 for 2-month supply"
                }
            }
        },
        "coq10": {
            "name": "Coenzyme Q10 (CoQ10)",
            "benefits": "Cellular energy production, antioxidant, heart health, anti-aging",
            "recommended_for": {
                "age_groups": ["40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["heart_health", "fatigue", "statin_users", "longevity"]
            },
            "dosage": {
                "40s": "100-200 mg daily",
                "50s": "100-200 mg daily",
                "60s": "100-300 mg daily",
                "70plus": "100-300 mg daily"
            },
            "contraindications": [],
            "interactions": ["blood_thinners", "insulin", "chemotherapy"],
            "sources": ["https://www.mayoclinic.org/drugs-supplements-coenzyme-q10/art-20362602"],
            "budget_tier": {
                "essential": {
                    "form": "Ubiquinone (regular CoQ10)",
                    "price_range": "$15-25 for 1-month supply"
                },
                "good": {
                    "form": "Ubiquinol (active form)",
                    "price_range": "$30-45 for 1-month supply"
                },
                "ideal": {
                    "form": "Ubiquinol with enhanced absorption (in oil base)",
                    "price_range": "$45-70 for 1-month supply"
                }
            }
        },
        "vitamin_k2": {
            "name": "Vitamin K2",
            "benefits": "Bone health, cardiovascular health, calcium regulation",
            "recommended_for": {
                "age_groups": ["40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["bone_health", "heart_health", "osteoporosis_risk", "longevity"]
            },
            "dosage": {
                "40s": "90-120 mcg daily",
                "50s": "90-180 mcg daily",
                "60s": "90-180 mcg daily",
                "70plus": "90-180 mcg daily"
            },
            "contraindications": [],
            "interactions": ["blood_thinners", "certain_antibiotics"],
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminK-HealthProfessional/"],
            "budget_tier": {
                "essential": {
                    "form": "K2 (MK-7) supplements",
                    "price_range": "$15-25 for 2-month supply"
                },
                "good": {
                    "form": "K2 (MK-7) with D3",
                    "price_range": "$25-40 for 2-month supply"
                },
                "ideal": {
                    "form": "Full-spectrum K2 (MK-4 and MK-7) with D3",
                    "price_range": "$40-60 for 2-month supply"
                }
            }
        },
        "taurine": {
            "name": "Taurine",
            "benefits": "Heart health, exercise performance, antioxidant, cognitive function",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["heart_health", "fitness_performance", "cognitive_function", "longevity"]
            },
            "dosage": {
                "20s": "500-2000 mg daily",
                "30s": "500-2000 mg daily",
                "40s": "500-3000 mg daily",
                "50s": "500-3000 mg daily",
                "60s": "500-3000 mg daily",
                "70plus": "500-3000 mg daily"
            },
            "contraindications": [],
            "interactions": ["lithium"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5933890/"],
            "budget_tier": {
                "essential": {
                    "form": "Taurine powder",
                    "price_range": "$10-15 for 2-month supply"
                },
                "good": {
                    "form": "Taurine capsules",
                    "price_range": "$15-25 for 2-month supply"
                },
                "ideal": {
                    "form": "Pharmaceutical-grade taurine with increased bioavailability",
                    "price_range": "$25-40 for 2-month supply"
                }
            }
        },
        "choline": {
            "name": "Choline",
            "benefits": "Brain health, liver function, metabolism, nervous system support",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["cognitive_function", "liver_health", "fitness_performance"]
            },
            "dosage": {
                "20s": "425-550 mg daily",
                "30s": "425-550 mg daily",
                "40s": "425-550 mg daily",
                "50s": "425-550 mg daily",
                "60s": "425-550 mg daily",
                "70plus": "425-550 mg daily"
            },
            "contraindications": ["trimethylaminuria"],
            "interactions": [],
            "sources": ["https://ods.od.nih.gov/factsheets/Choline-HealthProfessional/"],
            "budget_tier": {
                "essential": {
                    "form": "Choline bitartrate",
                    "price_range": "$10-20 for 2-month supply"
                },
                "good": {
                    "form": "Alpha-GPC or CDP-choline",
                    "price_range": "$25-40 for 1-month supply"
                },
                "ideal": {
                    "form": "Combination of Alpha-GPC and CDP-choline",
                    "price_range": "$40-60 for 1-month supply"
                }
            }
        },
        "zinc": {
            "name": "Zinc",
            "benefits": "Immune function, wound healing, DNA synthesis, taste and smell",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["immune_support", "skin_health", "reproductive_health"]
            },
            "dosage": {
                "20s": "8-11 mg daily",
                "30s": "8-11 mg daily",
                "40s": "8-11 mg daily",
                "50s": "8-11 mg daily",
                "60s": "8-11 mg daily",
                "70plus": "8-11 mg daily"
            },
            "contraindications": [],
            "interactions": ["antibiotics", "penicillamine", "copper_supplements"],
            "sources": ["https://ods.od.nih.gov/factsheets/Zinc-HealthProfessional/"],
            "budget_tier": {
                "essential": {
                    "form": "Zinc gluconate",
                    "price_range": "$5-10 for 3-month supply"
                },
                "good": {
                    "form": "Zinc picolinate",
                    "price_range": "$10-20 for 3-month supply"
                },
                "ideal": {
                    "form": "Zinc bisglycinate with copper",
                    "price_range": "$20-30 for 3-month supply"
                }
            }
        },
        "ashwagandha": {
            "name": "Ashwagandha",
            "benefits": "Stress reduction, anxiety relief, hormone balance, inflammation reduction",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["stress", "sleep_issues", "hormone_balance"]
            },
            "dosage": {
                "20s": "300-600 mg daily",
                "30s": "300-600 mg daily",
                "40s": "300-600 mg daily",
                "50s": "300-600 mg daily",
                "60s": "300-600 mg daily",
                "70plus": "300-600 mg daily"
            },
            "contraindications": ["autoimmune disorders", "pregnancy"],
            "interactions": ["sedatives", "thyroid_medication", "immunosuppressants"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6979308/"],
            "budget_tier": {
                "essential": {
                    "form": "Ashwagandha powder or basic extract",
                    "price_range": "$10-15 for 1-month supply"
                },
                "good": {
                    "form": "KSM-66 Ashwagandha (standardized extract)",
                    "price_range": "$20-30 for 1-month supply"
                },
                "ideal": {
                    "form": "Sensoril or high-potency full-spectrum extract",
                    "price_range": "$30-45 for 1-month supply"
                }
            }
        },
        "vitamin_e": {
            "name": "Vitamin E",
            "benefits": "Antioxidant protection, skin health, immune function",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["skin_health", "heart_health", "longevity"]
            },
            "dosage": {
                "20s": "15 mg (22.5 IU) daily",
                "30s": "15 mg (22.5 IU) daily",
                "40s": "15 mg (22.5 IU) daily",
                "50s": "15 mg (22.5 IU) daily",
                "60s": "15 mg (22.5 IU) daily",
                "70plus": "15 mg (22.5 IU) daily"
            },
            "contraindications": ["vitamin K deficiency", "bleeding disorders"],
            "interactions": ["blood_thinners", "certain_chemotherapy_drugs"],
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminE-HealthProfessional/"],
            "budget_tier": {
                "essential": {
                    "form": "Alpha-tocopherol",
                    "price_range": "$5-15 for 3-month supply"
                },
                "good": {
                    "form": "Mixed tocopherols",
                    "price_range": "$15-25 for 2-month supply"
                },
                "ideal": {
                    "form": "Full-spectrum vitamin E (tocopherols and tocotrienols)",
                    "price_range": "$25-40 for 2-month supply"
                }
            }
        },
        "creatine": {
            "name": "Creatine",
            "benefits": "Muscle strength, exercise performance, cognitive function, energy production",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["fitness_performance", "cognitive_function", "muscle_loss_prevention"]
            },
            "dosage": {
                "20s": "3-5 g daily",
                "30s": "3-5 g daily",
                "40s": "3-5 g daily",
                "50s": "3-5 g daily",
                "60s": "3-5 g daily",
                "70plus": "3-5 g daily"
            },
            "contraindications": ["kidney_disease"],
            "interactions": ["nephrotoxic_medications", "caffeine"],
            "sources": ["https://pubmed.ncbi.nlm.nih.gov/14561278/"],
            "budget_tier": {
                "essential": {
                    "form": "Creatine monohydrate powder",
                    "price_range": "$10-20 for 2-month supply"
                },
                "good": {
                    "form": "Micronized creatine monohydrate",
                    "price_range": "$20-30 for 2-month supply"
                },
                "ideal": {
                    "form": "Creapure® creatine monohydrate or creatine HCL",
                    "price_range": "$30-45 for 2-month supply"
                }
            }
        },
        "curcumin": {
            "name": "Curcumin (Turmeric Extract)",
            "benefits": "Anti-inflammatory, antioxidant, joint health, cognitive support",
            "recommended_for": {
                "age_groups": ["30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["joint_pain", "inflammation", "cognitive_function", "longevity"]
            },
            "dosage": {
                "30s": "500-1000 mg daily",
                "40s": "500-1000 mg daily",
                "50s": "500-1500 mg daily",
                "60s": "500-1500 mg daily",
                "70plus": "500-1500 mg daily"
            },
            "contraindications": ["gallbladder_disease", "bleeding_disorders"],
            "interactions": ["blood_thinners", "diabetes_medication"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5664031/"],
            "budget_tier": {
                "essential": {
                    "form": "Standard curcumin extract",
                    "price_range": "$10-20 for 1-month supply"
                },
                "good": {
                    "form": "Curcumin with piperine (black pepper extract)",
                    "price_range": "$20-35 for 1-month supply"
                },
                "ideal": {
                    "form": "High-bioavailability formulations (liposomal, phytosomal, or BCM-95)",
                    "price_range": "$35-60 for 1-month supply"
                }
            }
        },
        "vitamin_a": {
            "name": "Vitamin A",
            "benefits": "Vision health, immune function, skin health, cell growth",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["eye_health", "immune_support", "skin_health"]
            },
            "dosage": {
                "20s": "700-900 mcg RAE daily",
                "30s": "700-900 mcg RAE daily",
                "40s": "700-900 mcg RAE daily",
                "50s": "700-900 mcg RAE daily",
                "60s": "700-900 mcg RAE daily",
                "70plus": "700-900 mcg RAE daily"
            },
            "contraindications": ["pregnancy", "liver_disease"],
            "interactions": ["retinoid_medications", "certain_cholesterol_drugs"],
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminA-HealthProfessional/"],
            "budget_tier": {
                "essential": {
                    "form": "Beta-carotene (provitamin A)",
                    "price_range": "$5-10 for 3-month supply"
                },
                "good": {
