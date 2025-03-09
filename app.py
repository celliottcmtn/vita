4: "Very important, especially for your demographic",
                    5: "Essential for optimal health in your demographic"
                }
                st.markdown(f"**Priority**: {priority}/5 - {priority_text.get(priority, '')}")
                
                
                # Interaction warnings
                if supp_id in interactions:
                    st.markdown("### ⚠️ Potential Interactions")
                    for interaction in interactions[supp_id]:
                        st.markdown(f"- **{interaction['name']}**: {interaction['note']}")
                
                # Contraindications
                if supplement.get("contraindications"):
                    contraindications = [c.replace("_", " ").title() for c in supplement.get("contraindications", [])]
                    st.markdown(f"**Use caution if you have**: {', '.join(contraindications)}")
                
                # Display importance tiers if available
                if "importance_tier" in supplement:
                    st.markdown("### Recommended Forms")
                    
                    essential = supplement["importance_tier"].get("essential", {})
                    good = supplement["importance_tier"].get("good", {})
                    ideal = supplement["importance_tier"].get("ideal", {})
                    
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.markdown("**Essential**")
                        if essential:
                            st.markdown(f"Form: {essential.get('form', 'N/A')}")
                            st.markdown(f"Note: {essential.get('note', 'N/A')}")
                    
                    with col2:
                        st.markdown("**Good Value**")
                        if good:
                            st.markdown(f"Form: {good.get('form', 'N/A')}")
                            st.markdown(f"Note: {good.get('note', 'N/A')}")
                    
                    with col3:
                        st.markdown("**Ideal Choice**")
                        if ideal:
                            st.markdown(f"Form: {ideal.get('form', 'N/A')}")
                            st.markdown(f"Note: {ideal.get('note', 'N/A')}")
                            
                # Sources
                st.markdown("### Sources")
                for source in supplement.get("sources", []):
                    st.markdown(f"- [{source}]({source})")

def display_timing_guide(recommendations, age_group=None, gender=None, supplement_priorities=None, selected_priorities=None):
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
        # Skip if not in selected priorities
        if age_group and gender and supplement_priorities and selected_priorities:
            priority = get_priority_for_user(supp_id, age_group, gender, supplement_priorities)
            if priority not in selected_priorities:
                continue
                
        supplement = rec_data["supplement"]
        name = supplement["name"]
        
        if name in ["Iron"]:
            timing_categories["morning_empty_stomach"].append(name)
        elif name in ["Vitamin D", "Vitamin B12", "Omega-3 Fatty Acids", "Vitamin B1 (Thiamine)", "Vitamin A"]:
            timing_categories["morning_with_food"].append(name)
        elif name in ["Probiotics"]:
            timing_categories["morning_empty_stomach"].append(name)
        elif name in ["Vitamin C"]:
            timing_categories["afternoon"].append(name)
        elif name in ["Calcium"]:
            timing_categories["evening_with_food"].append(name)
        elif name in ["Magnesium"]:
            timing_categories["bedtime"].append(name)
        elif name in ["Zinc"]:
            timing_categories["morning_with_food"].append(name)
        elif name in ["Taurine"]:
            timing_categories["morning_with_food"].append(name)
        elif name in ["Choline"]:
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
    """)

def create_supplement_plan(recommendations, interactions, age_group, gender, supplement_priorities, selected_priorities=None):
    # No header here to avoid duplication
    
    if not recommendations:
        st.warning("No specific supplements recommended based on your selections.")
        return
    
    # If no priorities selected, include all
    if selected_priorities is None:
        selected_priorities = list(range(1, 6))  # Priorities 1-5
    
    # Create formatted plan
    plan_text = "# Your Personalized Supplement Plan\n\n"
    
    # Add information about the selected priority levels
    if len(selected_priorities) < 5:
        if len(selected_priorities) == 1 and 5 in selected_priorities:
            plan_text += "## Plan Type: Essential Supplements Only\n\n"
        elif set(selected_priorities) == {4, 5}:
            plan_text += "## Plan Type: Essential, Very Important Supplements\n\n"
        elif set(selected_priorities) == {3, 4, 5}:
            plan_text += "## Plan Type: Essential, Very Important, Important Supplements\n\n"
        else:
            included_levels = []
            if 5 in selected_priorities:
                included_levels.append("Essential")
            if 4 in selected_priorities:
                included_levels.append("Very Important")
            if 3 in selected_priorities:
                included_levels.append("Important")
            if 2 in selected_priorities:
                included_levels.append("Generally Beneficial")
            if 1 in selected_priorities:
                included_levels.append("Potentially Beneficial")
            
            plan_text += f"## Plan Type: {', '.join(included_levels)}\n\n"
    else:
        plan_text += "## Plan Type: Comprehensive (All Recommendations)\n\n"
    
    # Sort recommendations by priority
    sorted_recs = {}
    for supp_id, rec_data in recommendations.items():
        priority = get_priority_for_user(supp_id, age_group, gender, supplement_priorities)
        
        # Skip if not in selected priorities
        if priority not in selected_priorities:
            continue
            
        if priority not in sorted_recs:
            sorted_recs[priority] = []
        sorted_recs[priority].append((supp_id, rec_data))
    
    # Start with highest priority supplements
    for priority in sorted([p for p in sorted_recs.keys()], reverse=True):
        if priority == 5:
            plan_text += f"## Essential Supplements (Priority {priority}/5)\n\n"
        elif priority == 4:
            plan_text += f"## Very Important Supplements (Priority {priority}/5)\n\n"
        elif priority == 3:
            plan_text += f"## Important Supplements (Priority {priority}/5)\n\n"
        elif priority == 2:
            plan_text += f"## Generally Beneficial Supplements (Priority {priority}/5)\n\n"
        else:
            plan_text += f"## Potentially Beneficial Supplements (Priority {priority}/5)\n\n"
            
        for supp_id, rec_data in sorted_recs[priority]:
            supplement = rec_data["supplement"]
            
            plan_text += f"### {supplement['name']}\n"
            plan_text += f"- **Dosage:** {supplement['dosage'].get(age_group, 'Consult healthcare provider')}\n"
            
            # Hyperlink benefits to the first source if available
            if supplement.get('sources') and len(supplement['sources']) > 0:
                plan_text += f"- **Benefits:** [{supplement['benefits']}]({supplement['sources'][0]})\n"
            else:
                plan_text += f"- **Benefits:** {supplement['benefits']}\n"
            
            # Add importance recommendation
            if "importance_tier" in supplement:
                good_option = supplement["importance_tier"].get("good", {})
                if good_option:
                    plan_text += f"- **Recommended form:** {good_option.get('form', 'Standard form')}\n"
                    plan_text += f"- **Note:** {good_option.get('note', 'Standard form')}\n"
            
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
5. **Quality matters**: Look for supplements that have been third-party tested.

## Priority Rating System
🟢🟢🟢🟢🟢 - Essential for optimal health in your demographic
🟢🟢🟢🟢 - Very important, especially for your demographic
🟢🟢🟢 - Important for most people
🟢🟢 - Generally beneficial for wellness
🟢 - May provide minor benefits for some individuals

## Important Disclaimer
This supplement plan is provided for informational purposes only and is not a substitute for professional medical advice. Always consult with a healthcare provider before starting any supplement regimen, especially if you have health conditions or take medications.
"""
    
    # Display the plan and offer download
    st.markdown(plan_text)
    
    # In a real app, you would generate a PDF here
    st.download_button(
        label="Download Supplement Plan",
        data=plan_text,
        file_name="personalized_supplement_plan.txt",
        mime="text/plain"
    )

# ======== MAIN APPLICATION ========

def main():
    # Load data
    supplements_data, interactions_data, age_health_concerns, supplement_priorities = load_data()
    
    # Add a sidebar for navigation
    with st.sidebar:
        st.title("Navigation")
        page = st.radio(
            "Go to",
            ["Home & Recommendations", "Supplement Reference", "About"]
        )
    
    # Route to different pages based on sidebar selection
    if page == "Home & Recommendations":
        # Display header and get user information
        display_header()
        
        # Initialize or update recommendations
        if not st.session_state.plan_generated:
            age_group, gender, special_categories = get_user_info()
            
            # Get health concerns based on age and gender
            health_concerns = get_health_concerns(supplements_data, age_health_concerns, age_group, gender)
            
            # Store user info in session state
            st.session_state.user_info = {
                "age_group": age_group,
                "gender": gender,
                "special_categories": special_categories
            }
            st.session_state.health_concerns = health_concerns
            
            # Generate recommendations button
            if st.button("Generate Recommendations"):
                if not health_concerns:
                    st.warning("Please select at least one health concern for personalized recommendations.")
                else:
                    # Get recommendations based on user input
                    recommendations = get_recommended_supplements(supplements_data, age_group, gender, health_concerns)
                    
                    # Check for potential interactions
                    interactions = check_interactions(recommendations, interactions_data)
                    
                    # Store in session state
                    st.session_state.recommendations = recommendations
                    st.session_state.interactions = interactions
                    st.session_state.plan_generated = True
                    
                    # Use standard rerun
                    st.rerun()
        
        # Display recommendations if they exist
        if st.session_state.plan_generated and st.session_state.recommendations:
            # Retrieve data from session state
            recommendations = st.session_state.recommendations
            interactions = st.session_state.interactions
            user_info = st.session_state.user_info
            
            # Display recommendations
            display_recommendations(
                recommendations, 
                interactions, 
                user_info["age_group"], 
                user_info["gender"], 
                supplement_priorities, 
                user_info["special_categories"]
            )
            
            # Let user choose which priority levels to include in their plan
            st.header("Customize Your Supplement Plan")
            st.write("Choose which priority levels to include in your personalized plan:")
            
            # Create plan customization options based on available priorities
            age_group = user_info["age_group"]
            gender = user_info["gender"]
            special_categories = user_info["special_categories"]
            
            # Get all available priorities in the recommendations
            available_priorities = set()
            for supp_id in recommendations.keys():
                priority = get_priority_for_user(supp_id, age_group, gender, supplement_priorities)
                
                # Adjust for special categories
                if special_categories:
                    if special_categories.get("pregnant") and "pregnant_female" in supplement_priorities.get(supp_id, {}).get("age_gender_specific", {}):
                        priority = max(priority, supplement_priorities[supp_id]["age_gender_specific"]["pregnant_female"])
                    if special_categories.get("athlete") and f"athletes_{gender}" in supplement_priorities.get(supp_id, {}).get("age_gender_specific", {}):
                        priority = max(priority, supplement_priorities[supp_id]["age_gender_specific"][f"athletes_{gender}"])
                    if special_categories.get("statin_user") and "statin_users" in supplement_priorities.get(supp_id, {}).get("age_gender_specific", {}):
                        priority = max(priority, supplement_priorities[supp_id]["age_gender_specific"]["statin_users"])
                    if special_categories.get("antibiotic_user") and "antibiotic_users" in supplement_priorities.get(supp_id, {}).get("age_gender_specific", {}):
                        priority = max(priority, supplement_priorities[supp_id]["age_gender_specific"]["antibiotic_users"])
                    if special_categories.get("digestive_issues") and "digestive_issues" in supplement_priorities.get(supp_id, {}).get("age_gender_specific", {}):
                        priority = max(priority, supplement_priorities[supp_id]["age_gender_specific"]["digestive_issues"])
                
                available_priorities.add(priority)
            
            # Create options based on available priorities
            priority_options = []
            if 5 in available_priorities:
                priority_options.append({"label": "Essential Only (Priority 5)", "value": [5]})
            if 5 in available_priorities and 4 in available_priorities:
                priority_options.append({"label": "Essential + Very Important (Priority 5-4)", "value": [5, 4]})
            if 5 in available_priorities and 4 in available_priorities and 3 in available_priorities:
                priority_options.append({"label": "Essential + Very Important + Important (Priority 5-3)", "value": [5, 4, 3]})
            if available_priorities:
                priority_options.append({"label": "All Recommendations", "value": list(range(1, 6))})
            
            # Default to all priorities if no other options
            if not priority_options:
                priority_options.append({"label": "All Recommendations", "value": list(range(1, 6))})
            
            # Store selection in session state
            if 'plan_option' not in st.session_state:
                st.session_state.plan_option = len(priority_options) - 1  # Default to all recommendations
            
            # Let user select which plan they want
            selected_option_index = st.radio(
                "Select plan type:",
                options=range(len(priority_options)),
                format_func=lambda i: priority_options[i]["label"],
                index=st.session_state.plan_option,
                key="plan_type_radio",
                on_change=lambda: setattr(st.session_state, 'plan_option', st.session_state.plan_type_radio)
            )
            
            selected_priorities = priority_options[selected_option_index]["value"]
            
            # Generate plan button
            if st.button("Generate Customized Plan"):
                # Create and offer downloadable plan with selected priorities
                create_supplement_plan(
                    recommendations, 
                    interactions, 
                    age_group, 
                    gender, 
                    supplement_priorities, 
                    selected_priorities
                )
                
                # Update timing guide to match selected priorities
                display_timing_guide(recommendations, age_group, gender, supplement_priorities, selected_priorities)
            
            # Start over button
            if st.button("Start Over"):
                st.session_state.plan_generated = False
                st.session_state.recommendations = None
                st.session_state.interactions = None
                st.session_state.user_info = None
                st.session_state.health_concerns = None
                if 'plan_option' in st.session_state:
                    del st.session_state.plan_option
                st.rerun()
    
    elif page == "Supplement Reference":
        st.title("Supplement Reference Guide")
        st.write("Search for detailed information about specific supplements.")
        
        # Get all supplement names for the dropdown
        all_supplements = [(supp_id, data["name"]) for supp_id, data in supplements_data.items()]
        all_supplements.sort(key=lambda x: x[1])  # Sort by name
        
        selected_supplement = st.selectbox(
            "Select a supplement to learn more:",
            options=[s[0] for s in all_supplements],
            format_func=lambda x: next((s[1] for s in all_supplements if s[0] == x), x)
        )
        
        if selected_supplement:
            supp_data = supplements_data[selected_supplement]
            
            # Get priority rating
            priority = get_priority_for_user(selected_supplement, "40s", "female", supplement_priorities)  # Default to middle-aged female
            priority_display = display_priority_rating(priority)
            
            st.subheader(f"{supp_data['name']} {priority_display}")
            
            # Hyperlink benefits to the first source if available
            if supp_data.get('sources') and len(supp_data['sources']) > 0:
                st.markdown(f"**Benefits:** [{supp_data['benefits']}]({supp_data['sources'][0]})")
            else:
                st.write(f"**Benefits:** {supp_data['benefits']}")
            
            # Display age-specific dosages
            st.write("**Recommended Dosages by Age:**")
            dosage_data = []
            for age, dose in supp_data["dosage"].items():
                dosage_data.append({"Age Group": age, "Recommended Dosage": dose})
            
            st.table(pd.DataFrame(dosage_data))
            
            # Display contraindications
            if supp_data.get("contraindications"):
                st.write("**Contraindications:**")
                for contra in supp_data["contraindications"]:
                    st.write(f"- {contra.replace('_', ' ').title()}")
            
            # Display interactions
            if supp_data.get("interactions"):
                st.write("**Potential Interactions:**")
                for interact in supp_data["interactions"]:
                    st.write(f"- {interact.replace('_', ' ').title()}")
                    
            # Display sources
            if supp_data.get("sources"):
                st.write("**Sources:**")
                for source in supp_data["sources"]:
                    st.markdown(f"- [{source}]({source})")
    
    elif page == "About":
        st.title("About This App")
        st.write("""
        ## Personalized Supplement Advisor
        
        This application provides personalized supplement recommendations based on your age, gender, health concerns, and special categories.
        
        ### How It Works
        
        1. The app collects basic information about you (age, gender, health concerns, special categories)
        2. Based on scientific research, it suggests supplements that may benefit your specific profile
        3. The app assigns priority ratings (🟢) to help you understand which supplements are most important for you
        4. The app checks for potential interactions between supplements
        5. A timing guide helps you determine when to take each supplement for optimal effectiveness
        
        ### Priority Rating System
        
        🟢🟢🟢🟢🟢 - Essential for optimal health in your demographic  
        🟢🟢🟢🟢 - Very important, especially for your demographic  
        🟢🟢🟢 - Important for most people  
        🟢🟢 - Generally beneficial for wellness  
        🟢 - May provide minor benefits for some individuals
        
        ### Data Sources
        
        The recommendations in this application are based on peer-reviewed research and guidelines from reputable health organizations.
        Each supplement entry includes links to scientific sources.
        
        ### Disclaimer
        
        This tool provides general information only and is not a substitute for professional medical advice.
        Always consult with a healthcare provider before starting any supplement regimen.
        """)

    # Footer
    st.markdown("---")
    st.markdown("""
    **Disclaimer:** This application provides general information and is not a substitute for professional medical advice. 
    All recommendations should be reviewed with a healthcare provider before implementation.
    """)

if __name__ == "__main__":
    main()
