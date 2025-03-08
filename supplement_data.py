def get_supplement_data():
    """Return the comprehensive supplement database with 60+ entries"""
    
    supplements_data = {
        # Essential Vitamins
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
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminA-HealthProfessional/"]
        },
        "vitamin_b1": {
            "name": "Vitamin B1 (Thiamine)",
            "benefits": "Energy metabolism, nerve function, cognitive health",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["fatigue", "cognitive_function", "alcoholism_recovery", "nerve_health"]
            },
            "dosage": {
                "20s": "1.1-1.2 mg daily",
                "30s": "1.1-1.2 mg daily",
                "40s": "1.1-1.2 mg daily",
                "50s": "1.1-1.2 mg daily",
                "60s": "1.1-1.2 mg daily",
                "70plus": "1.1-1.2 mg daily"
            },
            "contraindications": [],
            "interactions": ["certain_diuretics"],
            "sources": ["https://ods.od.nih.gov/factsheets/Thiamin-HealthProfessional/"]
        },
        "vitamin_b2": {
            "name": "Vitamin B2 (Riboflavin)",
            "benefits": "Energy metabolism, cellular function, antioxidant activity",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["migraines", "fatigue", "eye_health", "energy_metabolism"]
            },
            "dosage": {
                "20s": "1.1-1.3 mg daily",
                "30s": "1.1-1.3 mg daily",
                "40s": "1.1-1.3 mg daily",
                "50s": "1.1-1.3 mg daily",
                "60s": "1.1-1.3 mg daily",
                "70plus": "1.1-1.3 mg daily"
            },
            "contraindications": [],
            "interactions": ["antacids", "tricyclic_antidepressants"],
            "sources": ["https://ods.od.nih.gov/factsheets/Riboflavin-HealthProfessional/"]
        },
        "vitamin_b3": {
            "name": "Vitamin B3 (Niacin)",
            "benefits": "Energy metabolism, skin health, cholesterol management",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["cholesterol_management", "skin_health", "energy_metabolism", "joint_mobility"]
            },
            "dosage": {
                "20s": "14-16 mg daily",
                "30s": "14-16 mg daily",
                "40s": "14-16 mg daily",
                "50s": "14-16 mg daily",
                "60s": "14-16 mg daily",
                "70plus": "14-16 mg daily"
            },
            "contraindications": ["liver_disease", "ulcers", "gout"],
            "interactions": ["statins", "diabetes_medications", "blood_pressure_medications"],
            "sources": ["https://ods.od.nih.gov/factsheets/Niacin-HealthProfessional/"]
        },
        "vitamin_b5": {
            "name": "Vitamin B5 (Pantothenic Acid)",
            "benefits": "Energy metabolism, hormone synthesis, stress response, skin health",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["stress", "energy_metabolism", "skin_health", "adrenal_support"]
            },
            "dosage": {
                "20s": "5 mg daily",
                "30s": "5 mg daily",
                "40s": "5 mg daily",
                "50s": "5 mg daily",
                "60s": "5 mg daily",
                "70plus": "5 mg daily"
            },
            "contraindications": [],
            "interactions": ["certain_antibiotics"],
            "sources": ["https://ods.od.nih.gov/factsheets/PantothenicAcid-HealthProfessional/"]
        },
        "vitamin_b6": {
            "name": "Vitamin B6 (Pyridoxine)",
            "benefits": "Protein metabolism, cognitive development, immune function, hemoglobin formation",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["pms_symptoms", "immune_support", "cognitive_function", "heart_health", "morning_sickness"]
            },
            "dosage": {
                "20s": "1.3 mg daily",
                "30s": "1.3 mg daily",
                "40s": "1.3 mg daily",
                "50s": "1.5-1.7 mg daily",
                "60s": "1.5-1.7 mg daily",
                "70plus": "1.5-1.7 mg daily"
            },
            "contraindications": ["high_doses_can_cause_neuropathy"],
            "interactions": ["certain_antibiotics", "anti_seizure_medications", "estrogen"],
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminB6-HealthProfessional/"]
        },
        "folate": {
            "name": "Folate (Vitamin B9)",
            "benefits": "DNA synthesis, cell division, red blood cell formation, neural tube development",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["pregnancy_support", "heart_health", "cognitive_function", "anemia", "depression"]
            },
            "dosage": {
                "20s": "400 mcg daily (600-800 mcg for pregnant women)",
                "30s": "400 mcg daily (600-800 mcg for pregnant women)",
                "40s": "400 mcg daily",
                "50s": "400 mcg daily",
                "60s": "400 mcg daily",
                "70plus": "400 mcg daily"
            },
            "contraindications": ["vitamin_b12_deficiency"],
            "interactions": ["methotrexate", "anticonvulsants", "sulfasalazine"],
            "sources": ["https://ods.od.nih.gov/factsheets/Folate-HealthProfessional/"]
        },
        "vitamin_b12": {
            "name": "Vitamin B12 (Cobalamin)",
            "benefits": "Nerve function, red blood cell formation, DNA synthesis, energy metabolism",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["fatigue", "vegetarian_vegan", "anemia", "cognitive_function", "nerve_health"]
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
            "interactions": ["metformin", "acid_reducers", "colchicine"],
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminB12-HealthProfessional/"]
        },
        "biotin": {
            "name": "Biotin (Vitamin B7)",
            "benefits": "Energy metabolism, hair health, skin health, nail strength",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["hair_health", "skin_health", "nail_health", "metabolism_support"]
            },
            "dosage": {
                "20s": "30 mcg daily",
                "30s": "30 mcg daily",
                "40s": "30 mcg daily",
                "50s": "30 mcg daily",
                "60s": "30 mcg daily",
                "70plus": "30 mcg daily"
            },
            "contraindications": [],
            "interactions": ["anticonvulsants", "can_interfere_with_lab_tests"],
            "sources": ["https://ods.od.nih.gov/factsheets/Biotin-HealthProfessional/"]
        },
        "vitamin_c": {
            "name": "Vitamin C",
            "benefits": "Immune support, antioxidant, collagen production, iron absorption",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["immune_support", "skin_health", "iron_deficiency", "longevity", "wound_healing"]
            },
            "dosage": {
                "20s": "75-90 mg daily",
                "30s": "75-90 mg daily",
                "40s": "75-90 mg daily",
                "50s": "75-90 mg daily",
                "60s": "75-90 mg daily",
                "70plus": "75-90 mg daily (up to 500-1000 mg for immune support)"
            },
            "contraindications": ["history_of_kidney_stones", "hemochromatosis"],
            "interactions": ["blood_thinners", "statins", "chemotherapy", "estrogen"],
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminC-HealthProfessional/"]
        },
        "vitamin_d": {
            "name": "Vitamin D",
            "benefits": "Bone health, immune function, mood regulation",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["bone_health", "immune_support", "depression", "longevity", "muscle_function"]
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
            "interactions": ["steroids", "weight_loss_drugs", "cholesterol_medication", "seizure_medications"],
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminD-HealthProfessional/"]
        },
        "vitamin_e": {
            "name": "Vitamin E",
            "benefits": "Antioxidant protection, skin health, immune function, heart and brain health",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["skin_health", "heart_health", "longevity", "cognitive_function", "immune_support"]
            },
            "dosage": {
                "20s": "15 mg (22.5 IU) daily",
                "30s": "15 mg (22.5 IU) daily",
                "40s": "15 mg (22.5 IU) daily",
                "50s": "15 mg (22.5 IU) daily",
                "60s": "15 mg (22.5 IU) daily",
                "70plus": "15 mg (22.5 IU) daily"
            },
            "contraindications": ["vitamin_k_deficiency", "bleeding_disorders"],
            "interactions": ["blood_thinners", "certain_chemotherapy_drugs", "statins"],
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminE-HealthProfessional/"]
        },
        "vitamin_k": {
            "name": "Vitamin K",
            "benefits": "Blood clotting, bone health, cardiovascular health, calcium regulation",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["bone_health", "heart_health", "osteoporosis_risk", "longevity", "blood_health"]
            },
            "dosage": {
                "20s": "90-120 mcg daily",
                "30s": "90-120 mcg daily",
                "40s": "90-120 mcg daily",
                "50s": "90-180 mcg daily",
                "60s": "90-180 mcg daily",
                "70plus": "90-180 mcg daily"
            },
            "contraindications": ["taking_warfarin"],
            "interactions": ["blood_thinners", "certain_antibiotics", "weight_loss_drugs", "vitamin_e"],
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminK-HealthProfessional/"]
        },
        # Minerals
        "calcium": {
            "name": "Calcium",
            "benefits": "Bone health, muscle function, nerve transmission, blood vessel function",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["bone_health", "osteoporosis_risk", "muscle_function", "heart_health"]
            },
            "dosage": {
                "20s": "1000 mg daily",
                "30s": "1000 mg daily",
                "40s": "1000 mg daily",
                "50s": "1200 mg daily",
                "60s": "1200 mg daily",
                "70plus": "1200 mg daily"
            },
            "contraindications": ["hypercalcemia", "kidney_stones", "certain_heart_conditions"],
            "interactions": ["iron_supplements", "thyroid_medication", "certain_antibiotics", "zinc", "magnesium"],
            "sources": ["https://ods.od.nih.gov/factsheets/Calcium-HealthProfessional/"]
        },
        "magnesium": {
            "name": "Magnesium",
            "benefits": "Muscle function, nerve function, energy production, sleep quality",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["muscle_cramps", "sleep_issues", "stress", "heart_health", "longevity", "bone_health"]
            },
            "dosage": {
                "20s": "310-400 mg daily",
                "30s": "310-420 mg daily",
                "40s": "320-420 mg daily",
                "50s": "320-420 mg daily",
                "60s": "320-420 mg daily",
                "70plus": "320-420 mg daily"
            },
            "contraindications": ["kidney_failure", "myasthenia_gravis"],
            "interactions": ["antibiotics", "diuretics", "heart_medication", "bisphosphonates"],
            "sources": ["https://ods.od.nih.gov/factsheets/Magnesium-HealthProfessional/"]
        },
        "zinc": {
            "name": "Zinc",
            "benefits": "Immune function, wound healing, DNA synthesis, taste and smell",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["immune_support", "skin_health", "reproductive_health", "wound_healing"]
            },
            "dosage": {
                "20s": "8-11 mg daily",
                "30s": "8-11 mg daily",
                "40s": "8-11 mg daily",
                "50s": "8-11 mg daily",
                "60s": "8-11 mg daily",
                "70plus": "8-11 mg daily"
            },
            "contraindications": ["excessive_supplementation"],
            "interactions": ["antibiotics", "penicillamine", "copper_supplements", "iron_supplements"],
            "sources": ["https://ods.od.nih.gov/factsheets/Zinc-HealthProfessional/"]
        },
        "iron": {
            "name": "Iron",
            "benefits": "Red blood cell formation, oxygen transport, energy metabolism",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s"],
                "genders": ["female", "prefer_not_to_say"],
                "health_concerns": ["anemia", "fatigue", "heavy_periods", "vegetarian_vegan"]
            },
            "dosage": {
                "20s": "18 mg daily (menstruating females), 8 mg daily (others)",
                "30s": "18 mg daily (menstruating females), 8 mg daily (others)",
                "40s": "18 mg daily (menstruating females), 8 mg daily (others)",
                "50s": "8-18 mg daily (depends on menopause status)",
                "60s": "8 mg daily",
                "70plus": "8 mg daily"
            },
            "contraindications": ["hemochromatosis", "thalassemia"],
            "interactions": ["calcium_supplements", "antacids", "certain_antibiotics", "vitamin_e"],
            "sources": ["https://ods.od.nih.gov/factsheets/Iron-HealthProfessional/"]
        },
        "selenium": {
            "name": "Selenium",
            "benefits": "Antioxidant protection, thyroid function, immune support, reproductive health",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["thyroid_health", "immune_support", "antioxidant_support", "heart_health", "male_fertility"]
            },
            "dosage": {
                "20s": "55 mcg daily",
                "30s": "55 mcg daily",
                "40s": "55 mcg daily",
                "50s": "55 mcg daily",
                "60s": "55 mcg daily",
                "70plus": "55 mcg daily"
            },
            "contraindications": ["excess_can_be_toxic"],
            "interactions": ["statins", "niacin", "chemotherapy_drugs"],
            "sources": ["https://ods.od.nih.gov/factsheets/Selenium-HealthProfessional/"]
        },
        "iodine": {
            "name": "Iodine",
            "benefits": "Thyroid function, metabolic regulation, cognitive development, immune support",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["thyroid_health", "energy_levels", "cognitive_function", "breast_health", "pregnancy_support"]
            },
            "dosage": {
                "20s": "150 mcg daily",
                "30s": "150 mcg daily",
                "40s": "150 mcg daily",
                "50s": "150 mcg daily",
                "60s": "150 mcg daily",
                "70plus": "150 mcg daily"
            },
            "contraindications": ["hashimotos_thyroiditis", "graves_disease"],
            "interactions": ["thyroid_medications", "lithium", "antithyroid_drugs"],
            "sources": ["https://ods.od.nih.gov/factsheets/Iodine-HealthProfessional/"]
        },
        "copper": {
            "name": "Copper",
            "benefits": "Iron metabolism, connective tissue formation, nerve function, antioxidant activity",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["joint_health", "cardiovascular_health", "hair_pigmentation", "energy_metabolism", "immune_support"]
            },
            "dosage": {
                "20s": "900 mcg daily",
                "30s": "900 mcg daily",
                "40s": "900 mcg daily",
                "50s": "900 mcg daily",
                "60s": "900 mcg daily",
                "70plus": "900 mcg daily"
            },
            "contraindications": ["wilson_disease"],
            "interactions": ["zinc_supplements", "vitamin_c_high_doses", "penicillamine"],
            "sources": ["https://ods.od.nih.gov/factsheets/Copper-HealthProfessional/"]
        },
        "manganese": {
            "name": "Manganese",
            "benefits": "Enzyme function, bone formation, blood clotting, inflammation reduction",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["bone_health", "metabolism", "joint_health", "blood_sugar_management", "antioxidant_support"]
            },
            "dosage": {
                "20s": "1.8-2.3 mg daily",
                "30s": "1.8-2.3 mg daily",
                "40s": "1.8-2.3 mg daily",
                "50s": "1.8-2.3 mg daily",
                "60s": "1.8-2.3 mg daily",
                "70plus": "1.8-2.3 mg daily"
            },
            "contraindications": ["liver_disease", "iron_deficiency_anemia"],
            "interactions": ["certain_antibiotics", "antacids", "iron_supplements"],
            "sources": ["https://ods.od.nih.gov/factsheets/Manganese-HealthProfessional/"]
        },
        "chromium": {
            "name": "Chromium",
            "benefits": "Blood sugar regulation, macronutrient metabolism, insulin sensitivity",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["blood_sugar_management", "weight_management", "energy_metabolism", "cardiovascular_health"]
            },
            "dosage": {
                "20s": "25-35 mcg daily",
                "30s": "25-35 mcg daily",
                "40s": "25-35 mcg daily",
                "50s": "25-35 mcg daily",
                "60s": "25-35 mcg daily",
                "70plus": "25-35 mcg daily"
            },
            "contraindications": ["kidney_disease", "liver_disease"],
            "interactions": ["insulin", "other_diabetes_medications", "NSAIDs", "beta_blockers"],
            "sources": ["https://ods.od.nih.gov/factsheets/Chromium-HealthProfessional/"]
        },
        "potassium": {
            "name": "Potassium",
            "benefits": "Blood pressure regulation, muscle function, nerve signaling, fluid balance",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["heart_health", "blood_pressure", "muscle_cramps", "exercise_recovery", "electrolyte_balance"]
            },
            "dosage": {
                "20s": "2500-3400 mg daily (from food and supplements)",
                "30s": "2500-3400 mg daily (from food and supplements)",
                "40s": "2500-3400 mg daily (from food and supplements)",
                "50s": "2500-3400 mg daily (from food and supplements)",
                "60s": "2500-3400 mg daily (from food and supplements)",
                "70plus": "2500-3400 mg daily (from food and supplements)"
            },
            "contraindications": ["kidney_disease", "taking_potassium_sparing_diuretics", "adrenal_insufficiency"],
            "interactions": ["ACE_inhibitors", "potassium_sparing_diuretics", "blood_pressure_medications", "nsaids"],
            "sources": ["https://ods.od.nih.gov/factsheets/Potassium-HealthProfessional/"]
        },
        "molybdenum": {
            "name": "Molybdenum",
            "benefits": "Enzyme function, detoxification, sulfite metabolism",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["detoxification_support", "sulfite_sensitivity", "liver_health", "alcohol_metabolism"]
            },
            "dosage": {
                "20s": "45 mcg daily",
                "30s": "45 mcg daily",
                "40s": "45 mcg daily",
                "50s": "45 mcg daily",
                "60s": "45 mcg daily",
                "70plus": "45 mcg daily"
            },
            "contraindications": ["gout"],
            "interactions": ["copper_absorption", "sulfite_containing_medications"],
            "sources": ["https://ods.od.nih.gov/factsheets/Molybdenum-HealthProfessional/"]
        },
        # Fatty Acids
        "omega_3": {
            "name": "Omega-3 Fatty Acids",
            "benefits": "Heart health, brain function, anti-inflammatory, joint support",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["heart_health", "joint_pain", "cognitive_function", "depression", "longevity", "inflammation"]
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
            "sources": ["https://ods.od.nih.gov/factsheets/Omega3FattyAcids-HealthProfessional/"]
        },
        "omega_6": {
            "name": "Omega-6 (GLA)",
            "benefits": "Skin health, hormonal balance, inflammation regulation",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["skin_health", "pms_symptoms", "hormone_balance", "inflammation", "eczema", "rheumatoid_arthritis"]
            },
            "dosage": {
                "20s": "500-1000 mg daily",
                "30s": "500-1000 mg daily",
                "40s": "500-1000 mg daily",
                "50s": "500-1000 mg daily",
                "60s": "500-1000 mg daily",
                "70plus": "500-1000 mg daily"
            },
            "contraindications": ["seizure_disorders", "bleeding_disorders"],
            "interactions": ["blood_thinners", "anti_inflammatory_drugs", "epilepsy_medications"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3257651/"]
        },
        "cla": {
            "name": "Conjugated Linoleic Acid (CLA)",
            "benefits": "Weight management, muscle retention, anti-inflammatory properties",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["weight_management", "body_composition", "inflammation", "metabolic_health"]
            },
            "dosage": {
                "20s": "3-6 g daily",
                "30s": "3-6 g daily",
                "40s": "3-6 g daily",
                "50s": "3-6 g daily",
                "60s": "3-6 g daily",
                "70plus": "3-6 g daily"
            },
            "contraindications": ["insulin_resistance", "diabetes", "metabolic_syndrome"],
            "interactions": ["diabetes_medications", "blood_pressure_medications"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2826589/"]
        },
        # Probiotics
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
            "interactions": ["antibiotics", "immunosuppressants"],
            "sources": ["https://www.nccih.nih.gov/health/probiotics-what-you-need-to-know"]
        },
        "prebiotics": {
            "name": "Prebiotics",
            "benefits": "Gut microbiome support, digestive health, immune function",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["digestive_issues", "gut_health", "immune_support", "weight_management"]
            },
            "dosage": {
                "20s": "3-5 g daily",
                "30s": "3-5 g daily",
                "40s": "3-5 g daily",
                "50s": "3-5 g daily",
                "60s": "3-5 g daily",
                "70plus": "3-5 g daily"
            },
            "contraindications": ["FODMAP_sensitivity", "certain_IBS_cases"],
            "interactions": [],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6041804/"]
        },
        # Antioxidants and Specialized Nutrients
        "coq10": {
            "name": "Coenzyme Q10 (CoQ10)",
            "benefits": "Cellular energy production, antioxidant, heart health, anti-aging",
            "recommended_for": {
                "age_groups": ["40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["heart_health", "fatigue", "statin_users", "longevity", "migraine_prevention", "gum_health", "exercise_performance"]
            },
            "dosage": {
                "40s": "100-200 mg daily",
                "50s": "100-200 mg daily",
                "60s": "100-300 mg daily",
                "70plus": "100-300 mg daily"
            },
            "contraindications": [],
            "interactions": ["blood_thinners", "insulin", "chemotherapy", "beta_blockers"],
            "sources": ["https://www.mayoclinic.org/drugs-supplements-coenzyme-q10/art-20362602"]
        },
        "alpha_lipoic_acid": {
            "name": "Alpha Lipoic Acid (ALA)",
            "benefits": "Antioxidant, glucose metabolism, nerve health, liver support",
            "recommended_for": {
                "age_groups": ["30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["nerve_health", "blood_sugar_management", "liver_health", "longevity", "skin_health", "metabolic_syndrome"]
            },
            "dosage": {
                "30s": "300-600 mg daily",
                "40s": "300-600 mg daily",
                "50s": "300-600 mg daily",
                "60s": "300-600 mg daily",
                "70plus": "300-600 mg daily"
            },
            "contraindications": ["thiamine_deficiency"],
            "interactions": ["diabetes_medications", "chemotherapy", "thyroid_medications", "vitamin_b1"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6723188/"]
        },
        "dhea": {
            "name": "DHEA",
            "benefits": "Hormone precursor, adrenal support, anti-aging, immune function",
            "recommended_for": {
                "age_groups": ["50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["hormone_balance", "bone_health", "adrenal_support", "longevity", "autoimmune_conditions", "mood_support"]
            },
            "dosage": {
                "50s": "25-50 mg daily",
                "60s": "25-50 mg daily",
                "70plus": "25-50 mg daily"
            },
            "contraindications": ["hormone_sensitive_cancers", "liver_disease", "PCOS", "pregnancy"],
            "interactions": ["hormone_therapies", "anticoagulants", "insulin", "antidepressants"],
            "sources": ["https://www.mayoclinic.org/drugs-supplements-dhea/art-20364199"]
        },
        "pqq": {
            "name": "Pyrroloquinoline Quinone (PQQ)",
            "benefits": "Mitochondrial biogenesis, neuroprotection, antioxidant, energy production",
            "recommended_for": {
                "age_groups": ["40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["heart_health", "cognitive_function", "energy_levels", "longevity", "mitochondrial_health"]
            },
            "dosage": {
                "40s": "10-20 mg daily",
                "50s": "10-20 mg daily",
                "60s": "10-20 mg daily",
                "70plus": "10-20 mg daily"
            },
            "contraindications": [],
            "interactions": ["blood_thinners", "certain_medications_metabolized_by_liver"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2908954/"]
        },
        "nac": {
            "name": "N-Acetyl Cysteine (NAC)",
            "benefits": "Antioxidant, liver support, respiratory health, detoxification",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["liver_health", "respiratory_health", "detoxification", "immune_support", "addiction_support", "mental_health"]
            },
            "dosage": {
                "20s": "600-1200 mg daily",
                "30s": "600-1200 mg daily",
                "40s": "600-1200 mg daily",
                "50s": "600-1200 mg daily",
                "60s": "600-1200 mg daily",
                "70plus": "600-1200 mg daily"
            },
            "contraindications": ["asthma_in_some_cases"],
            "interactions": ["nitroglycerin", "blood_thinners", "certain_cancer_medications"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5241507/"]
        },
        "melatonin": {
            "name": "Melatonin",
            "benefits": "Sleep regulation, antioxidant, immune modulation",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["sleep_issues", "jet_lag", "shift_work", "longevity", "seasonal_depression", "immune_support"]
            },
            "dosage": {
                "20s": "0.5-3 mg before bed",
                "30s": "0.5-3 mg before bed",
                "40s": "0.5-3 mg before bed",
                "50s": "0.5-5 mg before bed",
                "60s": "0.5-5 mg before bed",
                "70plus": "0.5-5 mg before bed"
            },
            "contraindications": ["autoimmune_disorders", "seizure_disorders", "depression", "pregnancy"],
            "interactions": ["blood_thinners", "immunosuppressants", "diabetes_medications", "contraceptives", "caffeine"],
            "sources": ["https://www.nccih.nih.gov/health/melatonin-what-you-need-to-know"]
        },
        "l_theanine": {
            "name": "L-Theanine",
            "benefits": "Stress reduction, focus with calmness, sleep quality, cognitive performance",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["stress", "anxiety", "sleep_issues", "focus", "cognitive_function"]
            },
            "dosage": {
                "20s": "100-400 mg daily",
                "30s": "100-400 mg daily",
                "40s": "100-400 mg daily",
                "50s": "100-400 mg daily",
                "60s": "100-400 mg daily",
                "70plus": "100-400 mg daily"
            },
            "contraindications": [],
            "interactions": ["blood_pressure_medications", "stimulants"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6836118/"]
        },
        "l_carnitine": {
            "name": "L-Carnitine",
            "benefits": "Energy production, recovery, heart health, exercise performance, brain function",
            "recommended_for": {
                "age_groups": ["30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["energy_levels", "heart_health", "exercise_performance", "brain_health", "vegetarian_vegan", "weight_management"]
            },
            "dosage": {
                "30s": "500-2000 mg daily",
                "40s": "500-2000 mg daily",
                "50s": "500-2000 mg daily",
                "60s": "1000-3000 mg daily",
                "70plus": "1000-3000 mg daily"
            },
            "contraindications": ["hypothyroidism", "seizure_disorders"],
            "interactions": ["thyroid_medications", "blood_thinners", "seizure_medications"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5872767/"]
        },
        "creatine": {
            "name": "Creatine",
            "benefits": "Muscle strength, exercise performance, cognitive function, energy production",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["muscle_strength", "exercise_performance", "cognitive_function", "energy_levels", "vegetarian_vegan", "muscle_preservation"]
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
            "interactions": ["nephrotoxic_medications", "diuretics", "NSAIDs"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6950288/"]
        },
        "collagen": {
            "name": "Collagen Peptides",
            "benefits": "Skin elasticity, joint health, bone strength, hair and nail support",
            "recommended_for": {
                "age_groups": ["30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["skin_health", "joint_pain", "bone_health", "hair_health", "nail_health", "gut_health", "wound_healing"]
            },
            "dosage": {
                "30s": "5-10 g daily",
                "40s": "10-15 g daily",
                "50s": "10-20 g daily",
                "60s": "10-20 g daily",
                "70plus": "10-20 g daily"
            },
            "contraindications": ["alpha-gal_syndrome", "certain_food_allergies"],
            "interactions": [],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6835901/"]
        },
        "maca": {
            "name": "Maca Root",
            "benefits": "Energy, hormone balance, libido, mood, fertility",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["energy_levels", "hormone_balance", "libido", "mood_support", "fertility", "menopause_symptoms"]
            },
            "dosage": {
                "20s": "1500-3000 mg daily",
                "30s": "1500-3000 mg daily",
                "40s": "1500-3000 mg daily",
                "50s": "1500-3000 mg daily",
                "60s": "1500-3000 mg daily",
                "70plus": "1500-3000 mg daily"
            },
            "contraindications": ["hormone_sensitive_conditions", "high_blood_pressure"],
            "interactions": ["hormone_therapies", "blood_pressure_medications", "thyroid_medications"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3614644/"]
        },
        "fiber": {
            "name": "Fiber Supplement",
            "benefits": "Digestive health, cholesterol management, blood sugar regulation",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["digestive_issues", "heart_health", "blood_sugar_management", "weight_management", "gut_microbiome_health", "colon_health"]
            },
            "dosage": {
                "20s": "5-10 g per serving, 25-38 g total daily",
                "30s": "5-10 g per serving, 25-38 g total daily",
                "40s": "5-10 g per serving, 25-38 g total daily",
                "50s": "5-10 g per serving, 25-38 g total daily",
                "60s": "5-10 g per serving, 25-38 g total daily",
                "70plus": "5-10 g per serving, 25-38 g total daily"
            },
            "contraindications": ["intestinal_narrowing", "difficulty_swallowing", "bowel_obstruction"],
            "interactions": ["diabetes_medications", "certain_antibiotics", "cholesterol_medications", "mineral_absorption"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3705355/"]
        },
        "taurine": {
            "name": "Taurine",
            "benefits": "Cardiovascular health, muscle function, antioxidant, energy production, neurological protection",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["heart_health", "exercise_performance", "energy_levels", "cognitive_function", "eye_health", "diabetes_risk", "muscle_function"]
            },
            "dosage": {
                "20s": "500-2000 mg daily",
                "30s": "500-2000 mg daily",
                "40s": "500-2000 mg daily",
                "50s": "500-3000 mg daily",
                "60s": "1000-3000 mg daily",
                "70plus": "1000-3000 mg daily"
            },
            "contraindications": ["bipolar_disorder_medications"],
            "interactions": ["certain_antipsychotics", "lithium", "certain_anticonvulsants"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8745570/", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5933890/"]
        },
        "choline": {
            "name": "Choline",
            "benefits": "Brain development, cognitive function, liver health, metabolism, nerve function, muscle movement",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["cognitive_function", "liver_health", "pregnancy_support", "nerve_health", "metabolic_health", "fatty_liver_disease", "muscle_recovery"]
            },
            "dosage": {
                "20s": "425-550 mg daily",
                "30s": "425-550 mg daily",
                "40s": "425-550 mg daily",
                "50s": "425-550 mg daily",
                "60s": "425-550 mg daily",
                "70plus": "425-550 mg daily"
            },
            "contraindications": ["trimethylaminuria", "atypical_odor_syndrome"],
            "interactions": ["methotrexate", "certain_anticonvulsants", "estrogen_therapies"],
            "sources": ["https://ods.od.nih.gov/factsheets/Choline-HealthProfessional/", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6259980/"]
        },
        "ashwagandha": {
            "name": "Ashwagandha",
            "benefits": "Stress reduction, thyroid support, muscle strength, cognitive function",
            "recommended_for": {
                "age_groups": ["20s", "30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["stress", "thyroid_health", "muscle_strength", "cognitive_function", "sleep_quality", "hormone_balance"]
            },
            "dosage": {
                "20s": "300-600 mg daily",
                "30s": "300-600 mg daily",
                "40s": "300-600 mg daily",
                "50s": "300-600 mg daily",
                "60s": "300-600 mg daily",
                "70plus": "300-600 mg daily"
            },
            "contraindications": ["pregnancy", "autoimmune_conditions", "certain_hormone_sensitive_cancers"],
            "interactions": ["thyroid_medications", "sedatives", "immunosuppressants", "blood_pressure_medications"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6979308/"]
        }
    }
    
    return supplements_data

def get_interactions_data():
    """Return the comprehensive interactions data for supplements"""
    
    interactions_data = {
        "calcium": ["iron", "zinc", "magnesium", "manganese"],
        "iron": ["calcium", "vitamin_e", "zinc", "green_tea", "quercetin"],
        "zinc": ["calcium", "iron", "copper", "folate", "tetracycline_antibiotics"],
        "magnesium": ["calcium", "potassium", "vitamin_d", "bisphosphonates", "fluoroquinolone_antibiotics"],
        "vitamin_c": ["vitamin_b12", "copper", "statins", "chemotherapy_drugs"],
        "vitamin_e": ["vitamin_k", "blood_thinners", "statins", "chemotherapy_drugs"],
        "vitamin_d": ["calcium", "magnesium", "corticosteroids", "weight_loss_drugs", "seizure_medications"],
        "vitamin_b12": ["vitamin_c", "acid_reducers", "metformin", "colchicine", "potassium_supplements"],
        "probiotics": ["antibiotics", "immunosuppressants", "antifungals"],
        "omega_3": ["blood_thinners", "vitamin_e", "ginkgo_biloba", "aspirin", "nsaids"],
        "vitamin_a": ["retinoid_medications", "certain_cholesterol_drugs", "tetracycline_antibiotics"],
        "vitamin_b1": ["certain_diuretics", "antacids"],
        "coq10": ["blood_thinners", "blood_pressure_medications", "chemotherapy_drugs", "insulin"],
        "vitamin_k": ["blood_thinners", "antibiotics", "weight_loss_drugs", "vitamin_e"],
        "chromium": ["nsaids", "antacids", "corticosteroids", "beta_blockers", "insulin"],
        "selenium": ["statins", "chemotherapy_drugs", "birth_control_pills"],
        "curcumin": ["blood_thinners", "nsaids", "diabetes_medications", "acid_blockers"],
        "berberine": ["diabetes_medications", "blood_thinners", "macrolide_antibiotics", "cyclosporine"],
        "ashwagandha": ["thyroid_medications", "immunosuppressants", "sedatives", "benzodiazepines"],
        "resveratrol": ["blood_thinners", "nsaids", "certain_medications_metabolized_by_liver", "estrogen_therapies"],
        "alpha_lipoic_acid": ["diabetes_medications", "chemotherapy", "thyroid_medications", "vitamin_b1"],
        "nac": ["nitrates", "blood_thinners", "activated_charcoal", "certain_cancer_medications"],
        "melatonin": ["blood_thinners", "immunosuppressants", "diabetes_medications", "contraceptives", "caffeine"],
        "dhea": ["hormone_therapies", "anticoagulants", "insulin", "antidepressants"],
        "ginseng": ["stimulants", "blood_thinners", "diabetes_medications", "antidepressants", "hormone_therapies"],
        "milk_thistle": ["estrogens", "diabetes_medications", "cytochrome_p450_medications", "psychiatric_drugs"],
        "l_theanine": ["stimulants", "sedatives", "blood_pressure_medications"],
        "ginkgo_biloba": ["blood_thinners", "maoi_antidepressants", "anticancer_drugs", "seizure_medications"],
        "creatine": ["caffeine", "nephrotoxic_drugs", "diuretics", "probenecid"],
        "rhodiola": ["stimulants", "ssris", "mao_inhibitors", "diabetes_medications"],
        "bacopa": ["anticholinergics", "calcium_channel_blockers", "thyroid_medications"],
        "glucosamine": ["blood_thinners", "diabetes_medications", "acetaminophen", "cancer_medications"]
    }
    
    return interactions_data

def get_age_health_concerns():
    """Return the expanded age and gender-specific health concerns"""
    
    age_health_concerns = {
        "20s": {
            "male": ["immune_support", "fitness_performance", "stress", "energy_levels", "mental_clarity", "digestive_health", "sleep_quality", "muscle_growth"],
            "female": ["immune_support", "iron_deficiency", "stress", "reproductive_health", "skin_health", "digestive_health", "sleep_quality", "hormone_balance"],
            "prefer_not_to_say": ["immune_support", "stress", "fitness_performance", "energy_levels", "digestive_health", "mental_clarity", "sleep_quality"]
        },
        "30s": {
            "male": ["energy_levels", "stress", "immune_support", "fitness_performance", "metabolism_support", "cardiovascular_health", "digestive_health", "fertility"],
            "female": ["energy_levels", "stress", "reproductive_health", "iron_deficiency", "metabolism_support", "skin_health", "digestive_health", "fertility"],
            "prefer_not_to_say": ["energy_levels", "stress", "immune_support", "fitness_performance", "metabolism_support", "digestive_health"]
        },
        "40s": {
            "male": ["heart_health", "energy_levels", "stress", "longevity", "weight_management", "prostate_health", "muscle_maintenance", "metabolic_health", "vision_support"],
            "female": ["energy_levels", "stress", "bone_health", "hormone_balance", "weight_management", "breast_health", "metabolic_health", "vision_support", "digestive_health"],
            "prefer_not_to_say": ["energy_levels", "stress", "heart_health", "longevity", "weight_management", "metabolic_health", "joint_health", "vision_support"]
        },
        "50s": {
            "male": ["heart_health", "prostate_health", "joint_pain", "cognitive_function", "longevity", "blood_sugar_balance", "vision_support", "stress_management", "immune_function"],
            "female": ["bone_health", "hormone_balance", "heart_health", "joint_pain", "longevity", "blood_sugar_balance", "vision_support", "weight_management", "cognitive_function"],
            "prefer_not_to_say": ["heart_health", "joint_pain", "cognitive_function", "longevity", "bone_health", "blood_sugar_balance", "vision_support", "stress_management"]
        },
        "60s": {
            "male": ["heart_health", "joint_pain", "cognitive_function", "prostate_health", "longevity", "bone_density", "muscle_preservation", "immune_resilience", "digestive_efficiency"],
            "female": ["bone_health", "heart_health", "joint_pain", "cognitive_function", "longevity", "bladder_function", "immune_resilience", "skin_elasticity", "vision_health"],
            "prefer_not_to_say": ["heart_health", "joint_pain", "cognitive_function", "longevity", "bone_health", "immune_resilience", "digestive_efficiency", "sleep_quality"]
        },
        "70plus": {
            "male": ["heart_health", "cognitive_function", "bone_health", "immune_support", "longevity", "digestive_function", "physical_mobility", "muscle_maintenance", "prostate_health", "vision_health"],
            "female": ["bone_health", "heart_health", "cognitive_function", "immune_support", "longevity", "physical_mobility", "digestive_function", "bladder_health", "vision_health", "skin_integrity"],
            "prefer_not_to_say": ["heart_health", "cognitive_function", "bone_health", "immune_support", "longevity", "physical_mobility", "digestive_function", "sleep_quality", "vision_health"]
        }
    }
    
    return age_health_concerns
