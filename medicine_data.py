MEDICINE_DATA = {
    "paracetamol": {
        "uses": "Used for pain and fever.",
        "interactions": ["warfarin"],
        "warning": "Long-term or excessive use may affect the liver."
    },

    "ibuprofen": {
        "uses": "Used for pain, inflammation and fever.",
        "interactions": ["warfarin", "aspirin"],
        "warning": "May increase the risk of stomach bleeding."
    },

    "warfarin": {
        "uses": "Blood thinner used to prevent blood clots.",
        "interactions": ["ibuprofen", "aspirin", "paracetamol"],
        "warning": "Can increase bleeding risk with some medicines."
    },

    "aspirin": {
        "uses": "Used for pain and, in some cases, prevention of blood clots.",
        "interactions": ["ibuprofen", "warfarin"],
        "warning": "May increase bleeding risk."
    }
}
