import streamlit as st
import pandas as pd
import supplement_data

# Set page configuration
st.set_page_config(
    page_title="Supplement Advisor",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply modern design styling with mobile fixes
st.markdown("""
<style>
    /* Modern color palette */
    :root {
        --primary: #007AFF;
        --secondary: #5AC8FA;
        --accent: #FF9500;
        --background: #F5F5F7;
        --card: #FFFFFF;
        --text: #1D1D1F;
        --text-secondary: #86868B;
        --success: #34C759;
        --warning: #FF9500;
        --error: #FF3B30;
        --border: #E5E5EA;
    }
    
    /* Base styling */
    .main {
        background-color: var(--background);
        color: var(--text) !important; /* Ensure text is dark on light background */
    }
    
    /* Make sure all text has proper contrast */
    h1, h2, h3, h4, p, label, div, span {
        color: var(--text) !important; /* Force dark text color */
    }
    
    .st-emotion-cache-eczf16 label, .st-emotion-cache-eczf16 p {
        color: var(--text) !important;
    }
    
    h1, h2, h3, h4 {
        font-family: SF Pro Display, -apple-system, BlinkMacSystemFont, sans-serif;
        font-weight: 600;
    }
    
    h1 {
        font-size: 2.5rem;
        margin-bottom: 1.5rem;
    }
    
    h2 {
        font-size: 1.8rem;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        border-bottom: 1px solid var(--border);
        padding-bottom: 0.5rem;
    }
    
    h3 {
        font-size: 1.3rem;
        margin-top: 1.2rem;
        margin-bottom: 0.8rem;
    }
    
    p {
        font-family: SF Pro Text, -apple-system, BlinkMacSystemFont, sans-serif;
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    
    /* Card styling */
    .stExpander {
        background-color: var(--card);
        border-radius: 10px !important;
        border: none !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1) !important;
        transition: all 0.2s ease;
    }
    
    .stExpander:hover {
        box-shadow: 0 4px 8px rgba(0,0,0,0.08) !important;
        transform: translateY(-1px);
    }
    
    /* Text within expanders */
    .stExpander * {
        color: var(--text) !important;
    }
    
    /* Button styling */
    .stButton button {
        background-color: var(--primary) !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 0.5rem 1rem !important;
        font-size: 1rem !important;
        font-weight: 500 !important;
        transition: all 0.2s ease !important;
    }
    
    .stButton button:hover {
        background-color: #0062CC !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1) !important;
    }
    
    /* Radio button styling */
    .stRadio > div {
        background-color: var(--card);
        border-radius: 10px;
        padding: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    
    /* Ensure radio buttons and their labels have contrast */
    .stRadio label {
        color: var(--text) !important;
    }
    
    /* Select box styling */
    .stSelectbox > div > div {
        border-radius: 8px !important;
        border: 1px solid var(--border) !important;
    }
    
    /* Dropdown text color */
    .stSelectbox label, .stSelectbox div {
        color: var(--text) !important;
    }
    
    /* Checkboxes */
    .stCheckbox label {
        color: var(--text) !important;
    }
    
    /* Sidebar styling */
    .css-1d391kg, .css-163ttbj {
        background-color: var(--card);
    }
    
    /* Ensure sidebar text is visible */
    .sidebar .sidebar-content, .sidebar .sidebar-content label, .sidebar .sidebar-content h1, .sidebar .sidebar-content p {
        color: var(--text) !important;
    }
    
    /* Table styling */
    .stTable table {
        color: var(--text) !important;
    }
    
    .stTable th, .stTable td {
        color: var(--text) !important;
    }
    
    /* Pill priorities with better contrast */
    .priority-pill-5 {
        background-color: var(--success);
        color: white !important; /* Make sure text is white on colored background */
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.8rem;
        display: inline-block;
        margin-left: 5px;
    }
    
    .priority-pill-4 {
        background-color: var(--primary);
        color: white !important;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.8rem;
        display: inline-block;
        margin-left: 5px;
    }
    
    .priority-pill-3 {
        background-color: var(--secondary);
        color: white !important;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.8rem;
        display: inline-block;
        margin-left: 5px;
    }
    
    .priority-pill-2 {
        background-color: var(--warning);
        color: white !important;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.8rem;
        display: inline-block;
        margin-left: 5px;
    }
    
    .priority-pill-1 {
        background-color: var(--text-secondary);
        color: white !important;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.8rem;
        display: inline-block;
        margin-left: 5px;
    }
    
    /* Fix for Streamlit dark mode */
    @media (prefers-color-scheme: dark) {
        :root {
            --text: #FFFFFF;
            --background: #1E1E1E;
            --card: #2D2D2D;
            --border: #3D3D3D;
        }
        
        /* Ensure proper contrast in dark mode */
        .stExpander, .stSelectbox, .stRadio, .stCheckbox {
            background-color: var(--card);
        }
        
        /* Make sure text remains visible */
        .stExpander *, .stSelectbox *, .stRadio *, .stCheckbox * {
            color: var(--text) !important;
        }
    }
    
    /* Mobile-specific overrides */
    @media (max-width: 768px) {
        /* Ensure text has strong contrast on mobile */
        body, p, h1, h2, h3, h4, label, div, span {
            color: var(--text) !important;
        }
        
        /* Ensure text in pills remains visible */
        .priority-pill-1, .priority-pill-2, .priority-pill-3, .priority-pill-4, .priority-pill-5 {
            color: white !important;
        }
        
        /* Adjust font sizes for mobile */
        h1 {
            font-size: 2rem;
        }
        
        h2 {
            font-size: 1.5rem;
        }
        
        h3 {
            font-size: 1.2rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for maintaining data between reruns
if 'recommendations' not in st.session_state:
    st.session_state.recommendations = None
if 'interactions' not in st.session_state:
    st.session_state.interactions = None
if 'user_info' not in st.session_state:
    st.session_state.user_info = None
if 'health_concerns' not in st.session_state:
    st.session_state.health_concerns = None
if 'plan_generated' not in st.session_state:
    st.session_state.plan_generated = False

# Load Data
def load_data():
    supplements_data = supplement_data.get_supplement_data()
    interactions_data = supplement_data.get_interactions_data()
    age_health_concerns = supplement_data.get_age_health_concerns()
    supplement_priorities = get_supplement_priorities()
    return supplements_data, interactions_data, age_health_concerns, supplement_priorities

# Priority Data
def get_supplement_priorities():
    """Return priority ratings (1-5) for supplements based on age group and gender
    
    Priority scale:
    1 - May provide minor benefits for some individuals
    2 - Generally beneficial for wellness
    3 - Important for most people
    4 - Very important, especially for specific demographics
    5 - Essential for optimal health in target demographics
    """
    
    supplement_priorities = {
        # Essential Vitamins
        "vitamin_a": {
            "default": 3,
            "age_gender_specific": {
                "20s_female": 3,
                "30s_female": 3,
                "pregnant_female": 4
            }
        },
        "vitamin_b1": {
            "default": 2,
            "age_gender_specific": {
                "40s_male": 3,
                "50s_male": 3,
                "60s_male": 3
            }
        },
        "vitamin_b2": {
            "default": 2,
            "age_gender_specific": {
                "30s_female": 3,
                "40s_female": 3
            }
        },
        "vitamin_b3": {
            "default": 3,
            "age_gender_specific": {
                "50s_male": 4,
                "60s_male": 4
            }
        },
        "vitamin_b5": {
            "default": 2
        },
        "vitamin_b6": {
            "default": 3,
            "age_gender_specific": {
                "20s_female": 4,
                "30s_female": 4,
                "40s_female": 4
            }
        },
        "folate": {
            "default": 3,
            "age_gender_specific": {
                "20s_female": 5,
                "30s_female": 5,
                "pregnant_female": 5
            }
        },
        "vitamin_b12": {
            "default": 4,
            "age_gender_specific": {
                "50s_male": 4,
                "50s_female": 4,
                "60s_male": 5,
                "60s_female": 5,
                "70plus_male": 5,
                "70plus_female": 5
            }
        },
        "biotin": {
            "default": 2
        },
        "vitamin_c": {
            "default": 4
        },
        "vitamin_d": {
            "default": 5,
            "age_gender_specific": {
                "50s_female": 5,
                "60s_female": 5,
                "70plus_female": 5,
                "50s_male": 5,
                "60s_male": 5,
                "70plus_male": 5
            }
        },
        "vitamin_e": {
            "default": 3
        },
        "vitamin_k": {
            "default": 3,
            "age_gender_specific": {
                "50s_female": 4,
                "60s_female": 4,
                "70plus_female": 4
            }
        },
        # Minerals
        "calcium": {
            "default": 3,
            "age_gender_specific": {
                "50s_female": 5,
                "60s_female": 5,
                "70plus_female": 5,
                "70plus_male": 4
            }
        },
        "magnesium": {
            "default": 4,
            "age_gender_specific": {
                "40s_female": 5,
                "50s_female": 5,
                "60s_female": 5,
                "70plus_female": 5,
                "40s_male": 4,
                "50s_male": 4,
                "60s_male": 5,
                "70plus_male": 5
            }
        },
        "zinc": {
            "default": 3,
            "age_gender_specific": {
                "50s_male": 4,
                "60s_male": 4,
                "70plus_male": 4
            }
        },
        "iron": {
            "default": 2,
            "age_gender_specific": {
                "20s_female": 4,
                "30s_female": 4,
                "40s_female": 4,
                "vegetarian_female": 5,
                "vegan_female": 5
            }
        },
        # Fatty Acids
        "omega_3": {
            "default": 4,
            "age_gender_specific": {
                "50s_male": 5,
                "60s_male": 5,
                "70plus_male": 5,
                "50s_female": 5,
                "60s_female": 5,
                "70plus_female": 5
            }
        },
        # Specialized Nutrients
        "coq10": {
            "default": 3,
            "age_gender_specific": {
                "50s_male": 4,
                "60s_male": 4,
                "70plus_male": 4,
                "50s_female": 4,
                "60s_female": 4,
                "70plus_female": 4,
                "statin_users": 5
            }
        },
        "probiotics": {
            "default": 3,
            "age_gender_specific": {
                "antibiotic_users": 5,
                "digestive_issues": 5
            }
        },
        # Added Supplements
        "taurine": {
            "default": 3,
            "age_gender_specific": {
                "20s_male": 4,
                "30s_male": 4, 
                "40s_male": 4,
                "athletes_male": 5,
                "athletes_female": 5,
                "60s_male": 4,
                "60s_female": 4,
                "70plus_male": 4,
                "70plus_female": 4
            }
        },
        "choline": {
            "default": 3,
            "age_gender_specific": {
                "20s_female": 4,
                "30s_female": 4,
                "pregnant_female": 5,
                "20s_male": 3,
                "30s_male": 3,
                "40s_male": 3,
                "40s_female": 3
            }
        },
    }
    
    return supplement_priorities

# Helper functions for priority system
def get_priority_for_user(supplement_id, age_group, gender, supplement_priorities):
    """Get the priority rating for a supplement based on user demographics"""
    
    if supplement_id not in supplement_priorities:
        return 1  # Minimum priority of 1 for all supplements
        
    priority_data = supplement_priorities[supplement_id]
    
    # Check for age and gender specific priority
    age_gender_key = f"{age_group}_{gender}"
    if "age_gender_specific" in priority_data and age_gender_key in priority_data["age_gender_specific"]:
        return priority_data["age_gender_specific"][age_gender_key]
    
    # Check for special categories like athletes or pregnant
    for special_key in ["athletes_male", "athletes_female", "pregnant_female", "vegetarian_female", "vegan_female", 
                        "antibiotic_users", "digestive_issues", "statin_users"]:
        if special_key.endswith(gender) and "age_gender_specific" in priority_data:
            if special_key in priority_data["age_gender_specific"]:
                # This would require additional UI elements to identify these special categories
                # For now, we'll skip these unless we add UI elements for them
                pass
    
    # Return default priority with a minimum of 1
    return max(priority_data.get("default", 1), 1)

def display_priority_rating(priority):
    """Create a visual representation of the priority rating"""
    if priority <= 0:
        return ""
    
    # Using green circle emoji for priority dots
    emoji_rating = "🟢" * priority
    
    # Add text description
    priority_descriptions = {
        1: "Potentially Beneficial",
        2: "Generally Beneficial",
        3: "Important",
        4: "Very Important",
        5: "Essential"
    }
    
    return f"{emoji_rating} ({priority_descriptions[priority]})"

# UI Functions
def display_header():
    st.title("Personalized Vitamin & Supplement Advisor")
    st.markdown("""
    This application provides personalized supplement recommendations based on your age, gender, and health concerns.
    
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
            ["Female", "Male", "Prefer Not to Say"]
        )
        # Convert to lowercase for backend processing
        gender = gender.lower()
    
    # Add special category options
    st.subheader("Special Categories (if applicable)")
    col1, col2 = st.columns(2)
    
    with col1:
        is_pregnant = st.checkbox("Pregnant or trying to conceive", value=False)
        is_vegetarian = st.checkbox("Vegetarian", value=False)
        is_athlete = st.checkbox("Athlete/High physical activity", value=False)
        
    with col2:
        is_statin_user = st.checkbox("Taking statin medications", value=False)
        is_antibiotic_user = st.checkbox("Recently used antibiotics", value=False)
        has_digestive_issues = st.checkbox("Experiencing digestive issues", value=False)
    
    special_categories = {
        "pregnant": is_pregnant,
        "vegetarian": is_vegetarian,
        "athlete": is_athlete,
        "statin_user": is_statin_user,
        "antibiotic_user": is_antibiotic_user,
        "digestive_issues": has_digestive_issues
    }
    
    return age_group, gender, special_categories

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
        "iron_deficiency": "Iron Deficiency",
        "skin_health": "Skin Health",
        "longevity": "Longevity/Anti-Aging",
        "reproductive_health": "Reproductive Health",
        "energy_levels": "Energy Levels",
        "fitness_performance": "Fitness Performance",
        "wound_healing": "Wound Healing",
        "digestive_issues": "Digestive Issues",
        "antibiotic_recovery": "Antibiotic Recovery",
        "vegetarian_vegan": "Vegetarian/Vegan Diet",
        "anemia": "Anemia",
        "heavy_periods": "Heavy Periods",
        "eye_health": "Eye Health",
        "alcoholism_recovery": "Alcoholism Recovery",
        "nerve_health": "Nerve Health",
        "muscle_function": "Muscle Function",
        "inflammation": "Inflammation",
        "prostate_health": "Prostate Health",
        "hormone_balance": "Hormone Balance",
        "weight_management": "Weight Management",
        "vision_support": "Vision Support",
        "metabolic_health": "Metabolic Health",
        "muscle_maintenance": "Muscle Maintenance",
        "blood_sugar_balance": "Blood Sugar Balance",
        "stress_management": "Stress Management",
        "immune_function": "Immune Function",
        "bone_density": "Bone Density",
        "muscle_preservation": "Muscle Preservation",
        "immune_resilience": "Immune Resilience",
        "digestive_efficiency": "Digestive Efficiency",
        "bladder_function": "Bladder Function",
        "skin_elasticity": "Skin Elasticity",
        "vision_health": "Vision Health",
        "physical_mobility": "Physical Mobility",
        "digestive_function": "Digestive Function",
        "bladder_health": "Bladder Health",
        "skin_integrity": "Skin Integrity",
        "mental_clarity": "Mental Clarity",
        "sleep_quality": "Sleep Quality",
        "muscle_growth": "Muscle Growth",
        "metabolism_support": "Metabolism Support",
        "cardiovascular_health": "Cardiovascular Health",
        "fertility": "Fertility Support",
        "diabetes_risk": "Diabetes Risk Management",
        "fatty_liver_disease": "Fatty Liver Disease",
        "muscle_recovery": "Muscle Recovery",
        "liver_health": "Liver Health"
    }
    
    # Convert technical terms to readable format for display
    display_concerns = {concern: concern_mapping.get(concern, concern.replace("_", " ").title()) 
                       for concern in all_health_concerns}
    
    # Create two sections
    st.subheader("Common Health Concerns for Your Age Group")
    st.write("Check all that apply to you:")
    
    # Show recommended concerns first with pre-selected checkboxes organized in columns
    selected_concerns = []
    
    # Organize common concerns in multiple columns
    num_columns = 3
    rec_concerns_columns = st.columns(num_columns)
    
    # Split recommended concerns across columns
    rec_concerns_split = [[] for _ in range(num_columns)]
    for i, concern in enumerate(recommended_concerns):
        if concern in display_concerns:
            rec_concerns_split[i % num_columns].append(concern)
    
    # Display concerns in each column
    for i, column in enumerate(rec_concerns_columns):
        with column:
            for concern in rec_concerns_split[i]:
                if concern in display_concerns:
                    label = display_concerns[concern]
                    if st.checkbox(label, value=False, key=f"rec_{concern}"):
                        selected_concerns.append(concern)
    
    # Create Additional health concerns section with dropdown
    st.subheader("Additional Health Concerns")
    
    # Other concerns (not in recommended)
    other_concerns = [c for c in all_health_concerns if c not in recommended_concerns]
    other_display = [display_concerns[concern] for concern in other_concerns]
    other_options = {display_concerns[c]: c for c in other_concerns}
    
    selected_other = st.multiselect(
        "Select any additional health concerns:",
        options=other_display,
        default=[]
    )
    selected_concerns.extend([other_options[sel] for sel in selected_other if sel in other_options])
    
    return selected_concerns

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

def check_interactions(recommendations, interactions_data):
    """Check for potential interactions between recommended supplements."""
    
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
        
        if interactions:
            potential_interactions[supp_id] = interactions
    
    return potential_interactions

def display_recommendations(recommendations, interactions, age_group, gender, supplement_priorities, special_categories=None):
    st.header("Your Personalized Supplement Recommendations")
    
    if not recommendations:
        st.warning("No specific supplements recommended based on your selections.")
        return
    
    # Create a dictionary to hold recommendations with their priorities
    prioritized_recs = {}
    
    # Calculate priority for each recommendation
    for supp_id, rec_data in recommendations.items():
        supplement = rec_data["supplement"]
        matching_concerns = rec_data["matching_concerns"]
        
        # Get priority rating for this supplement
        priority = get_priority_for_user(supp_id, age_group, gender, supplement_priorities)
        
        # Adjust priority for special categories if applicable
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
        
        # Add to priority group
        if priority not in prioritized_recs:
            prioritized_recs[priority] = []
        
        prioritized_recs[priority].append((supp_id, rec_data))
    
    # Display recommendations by priority (highest to lowest)
    for priority in sorted(prioritized_recs.keys(), reverse=True):
        priority_display = display_priority_rating(priority)
        
        if priority == 5:
            st.subheader(f"Essential Supplements {priority_display}")
        elif priority == 4:
            st.subheader(f"Very Important Supplements {priority_display}")
        elif priority == 3:
            st.subheader(f"Important Supplements {priority_display}")
        elif priority == 2:
            st.subheader(f"Generally Beneficial Supplements {priority_display}")
        else:
            st.subheader(f"Potentially Beneficial Supplements {priority_display}")
        
        for supp_id, rec_data in prioritized_recs[priority]:
            supplement = rec_data["supplement"]
            matching_concerns = rec_data["matching_concerns"]
            
            # Format concerns for display
            concern_display = [c.replace("_", " ").title() for c in matching_concerns]
            
            # Display name with expandable details
            with st.expander(f"**{supplement['name']}**"):
                # Main information with hyperlinked benefits
                if supplement.get('sources') and len(supplement['sources']) > 0:
