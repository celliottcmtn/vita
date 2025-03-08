"astaxanthin": {
            "name": "Astaxanthin",
            "benefits": "Powerful antioxidant, skin health, eye health, anti-inflammatory",
            "recommended_for": {
                "age_groups": ["30s", "40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["skin_health", "eye_health", "joint_pain", "exercise_recovery", "longevity", "brain_health", "cardiovascular_health"]
            },
            "dosage": {
                "30s": "4-12 mg daily",
                "40s": "4-12 mg daily",
                "50s": "4-12 mg daily",
                "60s": "4-12 mg daily",
                "70plus": "4-12 mg daily"
            },
            "contraindications": [],
            "interactions": ["hormone_therapies", "medications_metabolized_by_liver", "blood_pressure_medications"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5946307/"],
            "importance_tier": {
                "essential": {
                    "form": "Astaxanthin (4 mg)",
                    "note": "Basic antioxidant support"
                },
                "good": {
                    "form": "Astaxanthin with omega-3s",
                    "note": "Enhanced absorption with synergistic fatty acids"
                },
                "ideal": {
                    "form": "High-potency astaxanthin (12 mg) with lutein and zeaxanthin",
                    "note": "Comprehensive carotenoid complex for maximum benefits"
                }
            }
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
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6835901/"],
            "importance_tier": {
                "essential": {
                    "form": "Bovine collagen peptides",
                    "note": "Basic collagen support"
                },
                "good": {
                    "form": "Multi-type collagen complex (Types I, II, III, V, X)",
                    "note": "Comprehensive formula for multiple tissue types"
                },
                "ideal": {
                    "form": "Marine collagen with hyaluronic acid and vitamin C",
                    "note": "Highly bioavailable with synergistic ingredients for collagen synthesis"
                }
            }
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
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3705355/"],
            "importance_tier": {
                "essential": {
                    "form": "Psyllium husk powder",
                    "note": "Basic soluble fiber for gut and heart health"
                },
                "good": {
                    "form": "Mixed fiber blend (soluble and insoluble)",
                    "note": "Balanced formula for multiple benefits"
                },
                "ideal": {
                    "form": "Prebiotic fiber complex with digestive enzymes",
                    "note": "Advanced formula to feed beneficial bacteria and aid digestion"
                }
            }
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
        "iron": ["antacids", "calcium", "coffee", "dairy", "eggs", "tea", "soy", "zinc"],
        "berberine": ["diabetes_medications", "blood_thinners", "macrolide_antibiotics", "cyclosporine"],
        "ashwagandha": ["thyroid_medications", "immunosuppressants", "sedatives", "benzodiazepines"],
        "resveratrol": ["blood_thinners", "nsaids", "certain_medications_metabolized_by_liver", "estrogen_therapies"],
        "alpha_lipoic_acid": ["diabetes_medications", "chemotherapy", "thyroid_medications", "vitamin_b1"],
        "nac": ["nitrates", "blood_thinners", "activated_charcoal", "certain_cancer_medications"],
        "melatonin": ["blood_thinners", "immunosuppressants", "diabetes_medications", "contraceptives", "caffeine"],
        "dhea": ["hormone_therapies", "anticoagulants", "insulin", "antidepressants"],
        "ginseng": ["stimulants", "blood_thinners", "diabetes_medications", "antidepressants", "hormone_therapies"]
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
    
    return age_health_concernsdef get_supplement_data():
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
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminA-HealthProfessional/"],
            "importance_tier": {
                "essential": {
                    "form": "Beta-carotene (provitamin A)",
                    "note": "Basic form for general health maintenance"
                },
                "good": {
                    "form": "Chromium polynicotinate",
                    "note": "Better absorbed form with enhanced bioactivity"
                },
                "ideal": {
                    "form": "Chromium with cinnamon and alpha-lipoic acid",
                    "note": "Synergistic formula for blood sugar support"
                }
            }
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
            "sources": ["https://ods.od.nih.gov/factsheets/Molybdenum-HealthProfessional/"],
            "importance_tier": {
                "essential": {
                    "form": "Sodium molybdate",
                    "note": "Basic form for general supplementation"
                },
                "good": {
                    "form": "Molybdenum chelate",
                    "note": "Better absorbed by the body"
                },
                "ideal": {
                    "form": "Molybdenum in liver support complex",
                    "note": "Targeted formula for detoxification support"
                }
            }
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
            "sources": ["https://ods.od.nih.gov/factsheets/Potassium-HealthProfessional/"],
            "importance_tier": {
                "essential": {
                    "form": "Potassium citrate or gluconate (low dose, OTC)",
                    "note": "Basic form for general supplementation"
                },
                "good": {
                    "form": "Potassium with magnesium complex",
                    "note": "Synergistic combination for heart and muscle health"
                },
                "ideal": {
                    "form": "Potassium with electrolyte balance formula",
                    "note": "Complete electrolyte support with optimal absorption"
                }
            }
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
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3257651/"],
            "importance_tier": {
                "essential": {
                    "form": "Evening primrose oil",
                    "note": "Basic source of GLA"
                },
                "good": {
                    "form": "Borage oil (higher GLA)",
                    "note": "More concentrated source of GLA"
                },
                "ideal": {
                    "form": "Black currant seed oil with additional synergistic nutrients",
                    "note": "Balanced ratio of omega fatty acids with supporting nutrients"
                }
            }
        },
        "phosphatidylserine": {
            "name": "Phosphatidylserine",
            "benefits": "Cognitive function, memory, stress reduction, brain health",
            "recommended_for": {
                "age_groups": ["40s", "50s", "60s", "70plus"],
                "genders": ["male", "female", "prefer_not_to_say"],
                "health_concerns": ["cognitive_function", "memory_support", "stress", "exercise_recovery", "age_related_cognitive_decline"]
            },
            "dosage": {
                "40s": "100-300 mg daily",
                "50s": "100-300 mg daily",
                "60s": "100-300 mg daily",
                "70plus": "100-300 mg daily"
            },
            "contraindications": [],
            "interactions": ["blood_thinners", "cognitive_medications", "acetylcholinesterase_inhibitors"],
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4596514/"],
            "importance_tier": {
                "essential": {
                    "form": "Soy-derived phosphatidylserine",
                    "note": "Basic form for cognitive support"
                },
                "good": {
                    "form": "Sunflower-derived phosphatidylserine",
                    "note": "Non-soy alternative with good bioavailability"
                },
                "ideal": {
                    "form": "Sharp-PS® Green (sunflower lecithin) with DHA",
                    "note": "Premium form with synergistic omega-3 support"
                }
            }
        },
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
            "sources": ["https://www.mayoclinic.org/drugs-supplements-coenzyme-q10/art-20362602"],
            "importance_tier": {
                "essential": {
                    "form": "Ubiquinone (regular CoQ10)",
                    "note": "Basic form for general supplementation"
                },
                "good": {
                    "form": "Ubiquinol (active form)",
                    "note": "Pre-converted active form with better absorption for those over 40"
                },
                "ideal": {
                    "form": "Ubiquinol with enhanced absorption (in oil base)",
                    "note": "Maximum bioavailability with carrier oils for optimal absorption"
                }
            }
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
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6723188/"],
            "importance_tier": {
                "essential": {
                    "form": "Alpha lipoic acid",
                    "note": "Basic form for general antioxidant support"
                },
                "good": {
                    "form": "R-lipoic acid (more bioactive form)",
                    "note": "More potent isomer with better biological activity"
                },
                "ideal": {
                    "form": "Stabilized R-lipoic acid with biotin",
                    "note": "Enhanced stability with synergistic B-vitamin for metabolism"
                }
            }
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
            "sources": ["https://www.mayoclinic.org/drugs-supplements-dhea/art-20364199"],
            "importance_tier": {
                "essential": {
                    "form": "DHEA capsules",
                    "note": "Basic hormone support"
                },
                "good": {
                    "form": "Micronized DHEA",
                    "note": "Better absorption with smaller particle size"
                },
                "ideal": {
                    "form": "7-Keto DHEA (non-hormonal metabolite)",
                    "note": "Metabolite that doesn't convert to sex hormones but retains benefits"
                }
            }
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
            "sources": ["https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2908954/"],
            "importance_tier": {
                "essential": {
                    "form": "PQQ disodium salt",
                    "note": "Basic form for mitochondrial support"
                },
                "good": {
                    "form": "PQQ with CoQ10",
                    "note": "Synergistic combination for energy production"
                },
                "ideal": {
                    "form": "BioPQQ® with ubiquinol and other mitochondrial support nutrients",
                    "note": "Comprehensive formula for maximum mitochondrial benefits"
                }
            }
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
            "sources": ["https://www.nccih.nih.gov/health/melatonin-what-you-need-to-know"],
            "importance_tier": {
                "essential": {
                    "form": "Melatonin tablets",
                    "note": "Basic form for sleep support"
                },
                "good": {
                    "form": "Timed-release melatonin",
                    "note": "Sustained release for staying asleep"
                },
                "ideal": {
                    "form": "Liposomal melatonin with sleep-support nutrients",
                    "note": "Enhanced absorption with synergistic ingredients like magnesium and L-theanine"
                }
            }
        },
        "astaxanthin": {
            "name": "Astaxanthin",
            "benefits": "Powerful antioxidant, skin health, eye health, anti-inflammatory",
            "Mixed carotenoids with preformed vitamin A",
                    "note": "Better bioavailability and broader carotenoid spectrum"
                },
                "ideal": {
                    "form": "Full-spectrum vitamin A complex with fat-soluble cofactors",
                    "note": "Maximum bioavailability and synergistic effect with cofactors"
                }
            }
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
            "sources": ["https://ods.od.nih.gov/factsheets/Thiamin-HealthProfessional/"],
            "importance_tier": {
                "essential": {
                    "form": "Thiamine HCl",
                    "note": "Basic form sufficient for most people"
                },
                "good": {
                    "form": "Benfotiamine (fat-soluble form)",
                    "note": "Enhanced ability to cross cell membranes"
                },
                "ideal": {
                    "form": "Sulbutiamine or combination of thiamine forms",
                    "note": "Superior bioavailability and neurological benefits"
                }
            }
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
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminD-HealthProfessional/"],
            "importance_tier": {
                "essential": {
                    "form": "D3 tablets",
                    "note": "Basic supplementation for most people"
                },
                "good": {
                    "form": "D3 + K2 combination",
                    "note": "Synergistic effects for calcium metabolism"
                },
                "ideal": {
                    "form": "Liposomal D3 + K2 with organic oils",
                    "note": "Maximum absorption and utilization"
                }
            }
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
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminC-HealthProfessional/"],
            "importance_tier": {
                "essential": {
                    "form": "Ascorbic acid tablets",
                    "note": "Basic form for general immune support"
                },
                "good": {
                    "form": "Buffered vitamin C with bioflavonoids",
                    "note": "Gentler on stomach with enhanced absorption"
                },
                "ideal": {
                    "form": "Liposomal vitamin C or whole-food vitamin C complex",
                    "note": "Superior absorption and cellular delivery"
                }
            }
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
            "sources": ["https://ods.od.nih.gov/factsheets/Magnesium-HealthProfessional/"],
            "importance_tier": {
                "essential": {
                    "form": "Magnesium oxide",
                    "note": "Basic form with lower bioavailability"
                },
                "good": {
                    "form": "Magnesium citrate or glycinate",
                    "note": "Higher bioavailability with less GI distress"
                },
                "ideal": {
                    "form": "Magnesium threonate or glycinate complex with B6",
                    "note": "Superior bioavailability with brain and nervous system benefits"
                }
            }
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
            "sources": ["https://ods.od.nih.gov/factsheets/Zinc-HealthProfessional/"],
            "importance_tier": {
                "essential": {
                    "form": "Zinc gluconate",
                    "note": "Basic supplementation form"
                },
                "good": {
                    "form": "Zinc picolinate",
                    "note": "Enhanced absorption and utilization"
                },
                "ideal": {
                    "form": "Zinc bisglycinate with copper",
                    "note": "Highly bioavailable with balanced copper for safety"
                }
            }
        },
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
            "sources": ["https://ods.od.nih.gov/factsheets/Omega3FattyAcids-HealthProfessional/"],
            "importance_tier": {
                "essential": {
                    "form": "Fish oil capsules",
                    "note": "Basic omega-3 supplementation"
                },
                "good": {
                    "form": "Concentrated fish oil (higher EPA/DHA)",
                    "note": "More potent with higher omega-3 content"
                },
                "ideal": {
                    "form": "Triglyceride-form fish oil or algae-based (vegetarian)",
                    "note": "Superior bioavailability and purity"
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
            "interactions": ["antibiotics", "immunosuppressants"],
            "sources": ["https://www.nccih.nih.gov/health/probiotics-what-you-need-to-know"],
            "importance_tier": {
                "essential": {
                    "form": "Single-strain probiotics",
                    "note": "Basic gut support"
                },
                "good": {
                    "form": "Multi-strain probiotics (5-10 strains)",
                    "note": "Broader spectrum of beneficial bacteria"
                },
                "ideal": {
                    "form": "Shelf-stable multi-strain (10+ strains) with prebiotic",
                    "note": "Comprehensive microbiome support with food for probiotics"
                }
            }
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
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminB12-HealthProfessional/"],
            "importance_tier": {
                "essential": {
                    "form": "Cyanocobalamin tablets/capsules",
                    "note": "Basic form sufficient for most people"
                },
                "good": {
                    "form": "Methylcobalamin tablets",
                    "note": "Active form with better neural benefits"
                },
                "ideal": {
                    "form": "Sublingual methylcobalamin with intrinsic factor",
                    "note": "Superior absorption, especially for those with absorption issues"
                }
            }
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
            "sources": ["https://ods.od.nih.gov/factsheets/Iron-HealthProfessional/"],
            "importance_tier": {
                "essential": {
                    "form": "Ferrous sulfate",
                    "note": "Basic form with moderate absorption"
                },
                "good": {
                    "form": "Ferrous gluconate or ferrous glycinate",
                    "note": "Better absorbed with less GI distress"
                },
                "ideal": {
                    "form": "Iron bisglycinate chelate with vitamin C",
                    "note": "Maximum absorption with minimal side effects"
                }
            }
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
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminE-HealthProfessional/"],
            "importance_tier": {
                "essential": {
                    "form": "Alpha-tocopherol",
                    "note": "Basic form sufficient for general antioxidant support"
                },
                "good": {
                    "form": "Mixed tocopherols",
                    "note": "Broader spectrum of vitamin E components"
                },
                "ideal": {
                    "form": "Full-spectrum vitamin E (tocopherols and tocotrienols)",
                    "note": "Complete vitamin E complex with synergistic benefits"
                }
            }
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
            "sources": ["https://ods.od.nih.gov/factsheets/VitaminK-HealthProfessional/"],
            "importance_tier": {
                "essential": {
                    "form": "K2 (MK-7) supplements",
                    "note": "Basic form for bone and cardiovascular health"
                },
                "good": {
                    "form": "K2 (MK-7) with D3",
                    "note": "Synergistic combination for bone health"
                },
                "ideal": {
                    "form": "Full-spectrum K2 (MK-4 and MK-7) with D3",
                    "note": "Complete complex with optimal bioavailability"
                }
            }
        },
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
            "sources": ["https://ods.od.nih.gov/factsheets/Calcium-HealthProfessional/"],
            "importance_tier": {
                "essential": {
                    "form": "Calcium carbonate",
                    "note": "Basic form with good calcium content"
                },
                "good": {
                    "form": "Calcium citrate",
                    "note": "Better absorption, especially with low stomach acid"
                },
                "ideal": {
                    "form": "Calcium citrate with vitamin D3, K2, and magnesium",
                    "note": "Optimized formula for bone health and proper calcium utilization"
                }
            }
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
            "sources": ["https://ods.od.nih.gov/factsheets/Selenium-HealthProfessional/"],
            "importance_tier": {
                "essential": {
                    "form": "Sodium selenite",
                    "note": "Basic inorganic form"
                },
                "good": {
                    "form": "Selenium yeast or selenomethionine",
                    "note": "Organic form with better bioavailability"
                },
                "ideal": {
                    "form": "Selenium with vitamin E and other antioxidants",
                    "note": "Synergistic combination for maximum benefits"
                }
            }
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
            "sources": ["https://ods.od.nih.gov/factsheets/Iodine-HealthProfessional/"],
            "importance_tier": {
                "essential": {
                    "form": "Potassium iodide",
                    "note": "Basic form for thyroid support"
                },
                "good": {
                    "form": "Kelp extract",
                    "note": "Natural source with co-factors"
                },
                "ideal": {
                    "form": "Nascent iodine",
                    "note": "Highly bioavailable form for optimal absorption"
                }
            }
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
            "sources": ["https://ods.od.nih.gov/factsheets/Copper-HealthProfessional/"],
            "importance_tier": {
                "essential": {
                    "form": "Copper gluconate",
                    "note": "Basic form for general support"
                },
                "good": {
                    "form": "Copper bisglycinate",
                    "note": "Chelated form with better absorption"
                },
                "ideal": {
                    "form": "Copper with zinc balance formula",
                    "note": "Properly balanced with zinc for safety and efficacy"
                }
            }
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
            "sources": ["https://ods.od.nih.gov/factsheets/Manganese-HealthProfessional/"],
            "importance_tier": {
                "essential": {
                    "form": "Manganese sulfate",
                    "note": "Basic form for general supplementation"
                },
                "good": {
                    "form": "Manganese chelate",
                    "note": "Better absorbed and utilized"
                },
                "ideal": {
                    "form": "Manganese with other trace minerals",
                    "note": "Balanced with synergistic minerals for optimal benefits"
                }
            }
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
            "sources": ["https://ods.od.nih.gov/factsheets/Chromium-HealthProfessional/"],
            "importance_tier": {
                "essential": {
                    "form": "Chromium picolinate",
                    "note": "Common form with decent absorption"
                },
                "good": {
                    "form": "
