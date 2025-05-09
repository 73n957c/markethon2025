from typing import Dict, List, Tuple

from typing import Dict

class WasteClassificationService:
    WASTE_CLASSIFICATION = {
        "Recyclables": ["brown-glass", "green-glass", "white-glass", "cardboard", "metal", "paper", "plastic"],
        "Compostables": ["biological"],
        "Landfill Waste": ["trash"],
        "Hazardous Waste": ["battery"],
        "Special Disposal": ["clothes", "shoes"]
    }

    @staticmethod
    def get_waste_category(item: str) -> str:
        for category, items in WasteClassificationService.WASTE_CLASSIFICATION.items():
            if item in items:
                return category
        return "Unknown"

    @staticmethod
    def process_prediction_result(result_dict: Dict) -> Dict:
        if isinstance(result_dict, dict) and "prediction" in result_dict:
            predicted_item = result_dict["prediction"]
            waste_category = WasteClassificationService.get_waste_category(predicted_item)

            result_dict["waste_category"] = waste_category
            result_dict["disposal_message"] = f"This item ({predicted_item}) should be disposed of in the {waste_category} bin."

            guidelines = {
                "Recyclables": "Please make sure the item is clean and dry before recycling.",
                "Compostables": "Place in green bin for composting. No plastic bags allowed.",
                "Landfill Waste": "Place in black bin for general waste.",
                "Hazardous Waste": "Do not place in regular bins! Take to a hazardous waste collection point.",
                "Special Disposal": "Please take to a specialized collection point or donation center.",
                "Unknown": "Please consult local waste management guidelines."
            }
            result_dict["disposal_guidelines"] = guidelines.get(waste_category, "")

        return result_dict

from typing import Dict, List, Tuple

from typing import Dict

class WasteClassificationService:
    WASTE_CLASSIFICATION = {
        "Recyclables": ["brown-glass", "green-glass", "white-glass", "cardboard", "metal", "paper", "plastic"],
        "Compostables": ["biological"],
        "Landfill Waste": ["trash"],
        "Hazardous Waste": ["battery"],
        "Special Disposal": ["clothes", "shoes"]
    }

    @staticmethod
    def get_waste_category(item: str) -> str:
        for category, items in WasteClassificationService.WASTE_CLASSIFICATION.items():
            if item in items:
                return category
        return "Unknown"

    @staticmethod
    def process_prediction_result(result_dict: Dict) -> Dict:
        if isinstance(result_dict, dict) and "prediction" in result_dict:
            predicted_item = result_dict["prediction"]
            waste_category = WasteClassificationService.get_waste_category(predicted_item)

            result_dict["waste_category"] = waste_category
            result_dict["disposal_message"] = f"This item ({predicted_item}) should be disposed of in the {waste_category} bin."

            guidelines = {
                "Recyclables": "Please make sure the item is clean and dry before recycling.",
                "Compostables": "Place in green bin for composting. No plastic bags allowed.",
                "Landfill Waste": "Place in black bin for general waste.",
                "Hazardous Waste": "Do not place in regular bins! Take to a hazardous waste collection point.",
                "Special Disposal": "Please take to a specialized collection point or donation center.",
                "Unknown": "Please consult local waste management guidelines."
            }
            result_dict["disposal_guidelines"] = guidelines.get(waste_category, "")

        return result_dict
