"""
Treatment recommendations and disease information database.
Referenced in Chapter 3.5 (Output and Reporting) and Chapter 4.5.
"""

DISEASE_INFO = {
    # ── APPLE ──────────────────────────────────────────────────────────
    "Apple___Apple_scab": {
        "display_name": "Apple Scab",
        "crop": "Apple",
        "severity": "Moderate",
        "description": (
            "Apple scab is caused by the fungus Venturia inaequalis. "
            "It appears as olive-green to brown spots on leaves and fruit, "
            "leading to premature leaf drop and reduced fruit quality."
        ),
        "symptoms": [
            "Olive-green or brown spots on leaves",
            "Velvety texture on lesions",
            "Premature leaf drop",
            "Scabby, cracked fruit surface",
        ],
        "treatment": [
            "Apply fungicides (Captan or Mancozeb) at bud break",
            "Remove and destroy infected leaves and fruit",
            "Prune trees to improve air circulation",
            "Use resistant apple varieties when replanting",
        ],
        "prevention": "Apply preventive fungicide sprays during wet spring weather.",
    },
    "Apple___Black_rot": {
        "display_name": "Apple Black Rot",
        "crop": "Apple",
        "severity": "High",
        "description": (
            "Black rot is caused by the fungus Botryosphaeria obtusa. "
            "It causes leaf spots, fruit rot, and cankers on branches."
        ),
        "symptoms": [
            "Purple spots on leaves that enlarge with yellow halos",
            "Black, mummified fruit",
            "Cankers on branches with reddish-brown bark",
        ],
        "treatment": [
            "Prune and destroy infected branches and mummified fruit",
            "Apply copper-based fungicides",
            "Maintain tree vigor through proper fertilization",
            "Remove dead wood from the orchard",
        ],
        "prevention": "Sanitation is key — remove all mummified fruit before spring.",
    },
    "Apple___Cedar_apple_rust": {
        "display_name": "Cedar Apple Rust",
        "crop": "Apple",
        "severity": "Moderate",
        "description": (
            "Caused by Gymnosporangium juniperi-virginianae, this fungal disease "
            "requires both apple and cedar/juniper trees to complete its life cycle."
        ),
        "symptoms": [
            "Bright orange-yellow spots on upper leaf surface",
            "Tube-like structures on the underside of leaves",
            "Premature defoliation in severe cases",
        ],
        "treatment": [
            "Apply myclobutanil or mancozeb fungicides at pink bud stage",
            "Remove nearby cedar or juniper trees if possible",
            "Plant rust-resistant apple varieties",
        ],
        "prevention": "Spray fungicides from pink bud through petal fall.",
    },
    "Apple___healthy": {
        "display_name": "Healthy Apple",
        "crop": "Apple",
        "severity": "None",
        "description": "The apple plant appears healthy with no signs of disease.",
        "symptoms": [],
        "treatment": ["Continue regular monitoring and good agricultural practices"],
        "prevention": "Maintain proper irrigation, fertilization, and pruning schedules.",
    },

    # ── CORN ───────────────────────────────────────────────────────────
    "Corn___Cercospora_leaf_spot": {
        "display_name": "Corn Gray Leaf Spot (Cercospora)",
        "crop": "Corn",
        "severity": "High",
        "description": (
            "Gray leaf spot, caused by Cercospora zeae-maydis, is one of the most "
            "significant foliar diseases of corn worldwide."
        ),
        "symptoms": [
            "Rectangular, tan to gray lesions parallel to leaf veins",
            "Lesions surrounded by yellow halos",
            "Premature death of leaves in severe cases",
        ],
        "treatment": [
            "Apply strobilurin or triazole fungicides at tasseling",
            "Plant resistant hybrids",
            "Rotate crops with non-host plants",
            "Reduce crop residue through tillage",
        ],
        "prevention": "Crop rotation and resistant varieties are the most effective strategies.",
    },
    "Corn___Common_rust": {
        "display_name": "Corn Common Rust",
        "crop": "Corn",
        "severity": "Moderate",
        "description": (
            "Common rust is caused by Puccinia sorghi. It is most damaging "
            "when it occurs early in the season on susceptible hybrids."
        ),
        "symptoms": [
            "Small, circular to elongated cinnamon-brown pustules on both leaf surfaces",
            "Pustules turn dark brown/black as the season progresses",
            "Severe infections cause yellowing and death of leaves",
        ],
        "treatment": [
            "Apply fungicides (triazoles) if infection is severe before tasseling",
            "Plant resistant corn hybrids",
            "Scout fields regularly during the growing season",
        ],
        "prevention": "Use certified rust-resistant hybrid seeds.",
    },
    "Corn___Northern_Leaf_Blight": {
        "display_name": "Northern Corn Leaf Blight",
        "crop": "Corn",
        "severity": "High",
        "description": (
            "Caused by Exserohilum turcicum, Northern Leaf Blight can cause "
            "significant yield losses, especially when it occurs before silking."
        ),
        "symptoms": [
            "Long, elliptical, grayish-green to tan lesions (1–6 inches)",
            "Lesions may have wavy margins",
            "Entire leaves may die in severe infections",
        ],
        "treatment": [
            "Apply fungicides at early disease onset (before tasseling)",
            "Use resistant hybrids with Ht genes",
            "Practice crop rotation",
            "Bury or incorporate crop residue",
        ],
        "prevention": "Plant resistant varieties and rotate with soybeans or other non-hosts.",
    },
    "Corn___healthy": {
        "display_name": "Healthy Corn",
        "crop": "Corn",
        "severity": "None",
        "description": "The corn plant appears healthy with no signs of disease.",
        "symptoms": [],
        "treatment": ["Continue regular monitoring and good agricultural practices"],
        "prevention": "Maintain proper spacing, irrigation, and fertilization.",
    },

    # ── POTATO ─────────────────────────────────────────────────────────
    "Potato___Early_blight": {
        "display_name": "Potato Early Blight",
        "crop": "Potato",
        "severity": "Moderate",
        "description": (
            "Early blight is caused by Alternaria solani. It typically affects "
            "older leaves first and can cause significant defoliation."
        ),
        "symptoms": [
            "Dark brown spots with concentric rings (target-board pattern)",
            "Yellow halo surrounding the lesions",
            "Lesions start on older, lower leaves",
            "Premature defoliation",
        ],
        "treatment": [
            "Apply fungicides containing chlorothalonil or mancozeb",
            "Remove and destroy infected plant debris",
            "Ensure adequate plant nutrition (especially nitrogen)",
            "Avoid overhead irrigation",
        ],
        "prevention": "Use certified disease-free seed potatoes and practice crop rotation.",
    },
    "Potato___Late_blight": {
        "display_name": "Potato Late Blight",
        "crop": "Potato",
        "severity": "Critical",
        "description": (
            "Late blight, caused by Phytophthora infestans, is the most destructive "
            "potato disease. It was responsible for the Irish Potato Famine of the 1840s."
        ),
        "symptoms": [
            "Water-soaked, pale green lesions on leaves",
            "White, fuzzy mold on the underside of leaves in humid conditions",
            "Lesions turn brown/black rapidly",
            "Brown rot in tubers",
        ],
        "treatment": [
            "Apply systemic fungicides (metalaxyl, cymoxanil) immediately",
            "Destroy infected plants to prevent spread",
            "Avoid working in fields when plants are wet",
            "Harvest tubers promptly if disease is severe",
        ],
        "prevention": "Use resistant varieties and apply preventive fungicide sprays during cool, wet weather.",
    },
    "Potato___healthy": {
        "display_name": "Healthy Potato",
        "crop": "Potato",
        "severity": "None",
        "description": "The potato plant appears healthy with no signs of disease.",
        "symptoms": [],
        "treatment": ["Continue regular monitoring and good agricultural practices"],
        "prevention": "Use certified seed potatoes and practice 3-year crop rotation.",
    },

    # ── TOMATO ─────────────────────────────────────────────────────────
    "Tomato___Bacterial_spot": {
        "display_name": "Tomato Bacterial Spot",
        "crop": "Tomato",
        "severity": "High",
        "description": (
            "Bacterial spot is caused by Xanthomonas species. It affects leaves, "
            "stems, and fruit, causing significant yield and quality losses."
        ),
        "symptoms": [
            "Small, water-soaked spots on leaves",
            "Spots turn brown with yellow halos",
            "Raised, scab-like spots on fruit",
            "Defoliation in severe cases",
        ],
        "treatment": [
            "Apply copper-based bactericides",
            "Remove and destroy infected plant material",
            "Avoid overhead irrigation",
            "Use disease-free transplants",
        ],
        "prevention": "Use resistant varieties and copper sprays as a preventive measure.",
    },
    "Tomato___Early_blight": {
        "display_name": "Tomato Early Blight",
        "crop": "Tomato",
        "severity": "Moderate",
        "description": (
            "Caused by Alternaria solani, early blight is a common fungal disease "
            "that affects tomato plants, especially under warm, humid conditions."
        ),
        "symptoms": [
            "Dark brown spots with concentric rings on older leaves",
            "Yellow tissue surrounding the lesions",
            "Stem lesions (collar rot) near the soil line",
        ],
        "treatment": [
            "Apply fungicides (chlorothalonil, mancozeb, or copper)",
            "Remove infected lower leaves",
            "Mulch around plants to prevent soil splash",
            "Ensure proper plant spacing for air circulation",
        ],
        "prevention": "Rotate crops and use resistant tomato varieties.",
    },
    "Tomato___Late_blight": {
        "display_name": "Tomato Late Blight",
        "crop": "Tomato",
        "severity": "Critical",
        "description": (
            "Caused by Phytophthora infestans, late blight can destroy an entire "
            "tomato crop within days under favorable conditions."
        ),
        "symptoms": [
            "Large, irregular, water-soaked lesions on leaves",
            "White mold on the underside of leaves",
            "Brown, greasy-looking lesions on stems",
            "Firm, brown rot on fruit",
        ],
        "treatment": [
            "Apply systemic fungicides (metalaxyl + mancozeb) immediately",
            "Remove and bag infected plants — do not compost",
            "Avoid wetting foliage when irrigating",
        ],
        "prevention": "Monitor weather forecasts and apply preventive sprays during cool, wet periods.",
    },
    "Tomato___Leaf_Mold": {
        "display_name": "Tomato Leaf Mold",
        "crop": "Tomato",
        "severity": "Moderate",
        "description": (
            "Leaf mold is caused by Passalora fulva (formerly Fulvia fulva). "
            "It is most common in greenhouse tomatoes under high humidity."
        ),
        "symptoms": [
            "Pale green or yellow spots on upper leaf surface",
            "Olive-green to grayish-purple mold on the underside",
            "Leaves curl and wither in severe cases",
        ],
        "treatment": [
            "Reduce humidity by improving ventilation",
            "Apply fungicides (chlorothalonil or copper)",
            "Remove and destroy infected leaves",
        ],
        "prevention": "Maintain relative humidity below 85% and ensure good air circulation.",
    },
    "Tomato___Septoria_leaf_spot": {
        "display_name": "Tomato Septoria Leaf Spot",
        "crop": "Tomato",
        "severity": "Moderate",
        "description": (
            "Septoria leaf spot, caused by Septoria lycopersici, is one of the most "
            "destructive diseases of tomato foliage."
        ),
        "symptoms": [
            "Numerous small, circular spots with dark borders and gray centers",
            "Tiny black dots (pycnidia) visible in the center of spots",
            "Yellowing and dropping of infected leaves",
        ],
        "treatment": [
            "Apply fungicides (chlorothalonil, mancozeb, or copper) at first sign",
            "Remove infected leaves immediately",
            "Avoid overhead watering",
            "Mulch to prevent soil splash",
        ],
        "prevention": "Practice crop rotation and use disease-free transplants.",
    },
    "Tomato___Spider_mites": {
        "display_name": "Tomato Spider Mites (Two-spotted)",
        "crop": "Tomato",
        "severity": "Moderate",
        "description": (
            "Two-spotted spider mites (Tetranychus urticae) are tiny arachnids "
            "that feed on plant cells, causing stippling and bronzing of leaves."
        ),
        "symptoms": [
            "Fine stippling (tiny yellow/white dots) on upper leaf surface",
            "Bronze or silvery discoloration of leaves",
            "Fine webbing on the underside of leaves",
            "Leaf drop in severe infestations",
        ],
        "treatment": [
            "Apply miticides (abamectin, bifenazate) or insecticidal soap",
            "Spray the underside of leaves thoroughly",
            "Introduce predatory mites (Phytoseiulus persimilis) for biological control",
            "Increase humidity — mites thrive in dry conditions",
        ],
        "prevention": "Avoid water stress and dusty conditions that favor mite outbreaks.",
    },
    "Tomato___Target_Spot": {
        "display_name": "Tomato Target Spot",
        "crop": "Tomato",
        "severity": "Moderate",
        "description": (
            "Target spot is caused by Corynespora cassiicola. It affects leaves, "
            "stems, and fruit, and is favored by warm, humid conditions."
        ),
        "symptoms": [
            "Brown lesions with concentric rings (target pattern)",
            "Yellow halo around lesions",
            "Lesions on fruit appear as dark, sunken spots",
        ],
        "treatment": [
            "Apply fungicides (azoxystrobin, chlorothalonil)",
            "Improve air circulation through pruning",
            "Avoid overhead irrigation",
        ],
        "prevention": "Use resistant varieties and practice crop rotation.",
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "display_name": "Tomato Yellow Leaf Curl Virus (TYLCV)",
        "crop": "Tomato",
        "severity": "Critical",
        "description": (
            "TYLCV is a devastating viral disease transmitted by the silverleaf "
            "whitefly (Bemisia tabaci). It can cause up to 100% yield loss."
        ),
        "symptoms": [
            "Upward curling and yellowing of young leaves",
            "Stunted plant growth",
            "Flower drop and poor fruit set",
            "Small, crumpled leaves",
        ],
        "treatment": [
            "No cure exists — remove and destroy infected plants immediately",
            "Control whitefly populations with insecticides (imidacloprid)",
            "Use yellow sticky traps to monitor whitefly populations",
            "Apply reflective mulches to repel whiteflies",
        ],
        "prevention": "Plant TYLCV-resistant varieties and use insect-proof nets in nurseries.",
    },
    "Tomato___Tomato_mosaic_virus": {
        "display_name": "Tomato Mosaic Virus (ToMV)",
        "crop": "Tomato",
        "severity": "High",
        "description": (
            "Tomato mosaic virus is a highly contagious virus spread by contact "
            "with infected plant material, tools, and hands."
        ),
        "symptoms": [
            "Mosaic pattern of light and dark green on leaves",
            "Leaf distortion and curling",
            "Stunted growth",
            "Mottled or streaked fruit",
        ],
        "treatment": [
            "No chemical cure — remove and destroy infected plants",
            "Disinfect tools with 10% bleach solution between plants",
            "Wash hands thoroughly before handling plants",
        ],
        "prevention": "Use virus-free certified seeds and resistant varieties.",
    },
    "Tomato___healthy": {
        "display_name": "Healthy Tomato",
        "crop": "Tomato",
        "severity": "None",
        "description": "The tomato plant appears healthy with no signs of disease.",
        "symptoms": [],
        "treatment": ["Continue regular monitoring and good agricultural practices"],
        "prevention": "Maintain proper irrigation, staking, and fertilization schedules.",
    },
}


def get_disease_info(class_name: str) -> dict:
    """Returns disease information for a given class name."""
    return DISEASE_INFO.get(
        class_name,
        {
            "display_name": class_name.replace("_", " "),
            "crop": "Unknown",
            "severity": "Unknown",
            "description": "No detailed information available for this class.",
            "symptoms": [],
            "treatment": ["Consult a local agricultural expert for advice."],
            "prevention": "Practice general good agricultural practices.",
        },
    )


SEVERITY_COLORS = {
    "None":     "#28a745",   # green
    "Moderate": "#ffc107",   # yellow
    "High":     "#fd7e14",   # orange
    "Critical": "#dc3545",   # red
    "Unknown":  "#6c757d",   # gray
}
