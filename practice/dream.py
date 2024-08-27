import json
import random

def generate_dream_data(num_entries):
    emotions = [
        "화남", "행복", "슬픔", "두려움", "기대", "혼란"
    ]
    
    # Detailed interpretations for each emotion
    interpretations = {
        "화남": [
            ("이 꿈은 당신이 현재 상황에서 큰 불만이나 분노를 느끼고 있다는 것을 나타냅니다. 특히, 주변 사람들과의 갈등이 원인일 수 있습니다.", "심리 상담"),
            ("이 꿈은 당신이 최근에 중요한 일이 제대로 진행되지 않아 불만을 느끼고 있음을 나타냅니다. 감정을 관리하는 방법을 찾아보세요.", "명상"),
            ("이 꿈은 당신이 자신이 원하는 방향으로 일이 진행되지 않아서 화가 나 있는 상태를 의미할 수 있습니다. 해결책을 모색해보세요.", "운동")
        ],
        "행복": [
            ("이 꿈은 당신이 긍정적인 감정을 느끼고 있으며, 현재 삶에 만족하고 있음을 보여줍니다. 친구나 가족과의 시간도 긍정적인 영향을 미칩니다.", "자기 개발 서적"),
            ("이 꿈은 당신의 현재 상태가 매우 안정적이고, 삶의 여러 측면에서 만족감을 느끼고 있음을 나타냅니다.", "사회적 활동"),
            ("이 꿈은 당신의 목표가 잘 이루어지고 있는 상태를 반영합니다. 앞으로의 계획도 긍정적일 것입니다.", "자기 개발 서적")
        ],
        "슬픔": [
            ("이 꿈은 당신이 최근에 슬픔을 겪고 있거나 감정적으로 힘든 상황에 처해 있음을 의미할 수 있습니다. 과거의 상처가 영향을 미칠 수 있습니다.", "심리 상담"),
            ("이 꿈은 현재의 감정적인 상태가 좋지 않으며, 내면의 불안이나 스트레스가 해소되지 않았다는 것을 의미합니다.", "명상"),
            ("이 꿈은 당신이 감정적으로 치유가 필요하며, 자신을 돌보는 시간이 필요하다는 것을 나타냅니다.", "운동")
        ],
        "두려움": [
            ("이 꿈은 현재의 상황에 대한 두려움이나 불안을 표현하고 있을 수 있습니다. 미래에 대한 걱정이 반영된 것일 수 있습니다.", "심리 상담"),
            ("이 꿈은 당신이 불확실한 상황에서 불안감을 느끼고 있으며, 이로 인해 정신적으로 힘들어하는 상태를 나타냅니다.", "명상"),
            ("이 꿈은 당신이 불안한 상황에서 벗어나기 위한 해결책을 찾아야 한다는 것을 의미할 수 있습니다.", "운동")
        ],
        "기대": [
            ("이 꿈은 미래에 대한 기대감이나 새로운 시작에 대한 희망을 나타냅니다. 긍정적인 변화가 있을 것입니다.", "운동"),
            ("이 꿈은 당신이 새로운 기회를 맞이하고 있으며, 앞으로의 계획에 대해 긍정적인 전망을 가지고 있다는 것을 의미합니다.", "자기 개발 서적"),
            ("이 꿈은 당신이 다가오는 미래에 대해 희망을 가지고 있으며, 큰 목표를 향해 나아가고 있다는 것을 보여줍니다.", "사회적 활동")
        ],
        "혼란": [
            ("이 꿈은 현재 상황에 대한 혼란스러운 감정이나 불확실성을 반영할 수 있습니다. 많은 결정들이 필요할 수 있습니다.", "사회적 활동"),
            ("이 꿈은 당신이 상황을 명확히 이해하지 못하고 있음을 의미하며, 현재의 불확실성이 불안감을 초래하고 있습니다.", "심리 상담"),
            ("이 꿈은 당신이 현재의 상황에서 방향을 잃고 혼란스러움을 느끼고 있다는 것을 나타냅니다. 차분히 상황을 정리해보세요.", "명상")
        ]
    }
    
    # Detailed activities for each recommended activity
    activities = {
        "심리 상담": "전문가와의 상담을 통해 현재의 감정 문제를 해결할 수 있습니다. 전문가의 도움을 받으면 감정적인 안정감을 찾는 데 도움이 됩니다.",
        "자기 개발 서적": "긍정적인 감정을 유지하고, 자기 자신을 더 잘 이해하기 위해 자기 개발 서적을 읽어보세요. 유용한 조언과 방법이 포함되어 있습니다.",
        "명상": "명상은 마음을 진정시키고 스트레스를 줄이는 데 도움이 됩니다. 매일 조금씩 명상하는 습관을 들이면 정신적 안정을 찾는 데 도움이 될 것입니다.",
        "운동": "정기적인 운동은 스트레스를 해소하고 기분을 좋게 하는 데 도움이 됩니다. 운동은 신체와 정신 모두에 긍정적인 영향을 미칩니다.",
        "사회적 활동": "친구들과의 만남이나 사회적 활동을 통해 긍정적인 감정을 유지하세요. 사회적 관계는 정서적인 안정감을 제공할 수 있습니다."
    }
    
    data = []
    
    for i in range(num_entries):
        dream_id = f"D{i+1:04d}"
        emotion = random.choice(emotions)
        interpretation = random.choice(interpretations[emotion])
        interpretation_description, recommended_activity = interpretation
        activity_description = activities[recommended_activity]
        
        data.append({
            "dream_id": dream_id,
            "emotion": emotion,
            "interpretation_description": interpretation_description,
            "recommended_activity": recommended_activity,
            "activity_description": activity_description
        })
    
    return data

# Generate 1000 entries
dream_data = generate_dream_data(1000)

# Save to JSON file
output_file = 'dream_data.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(dream_data, f, ensure_ascii=False, indent=4)

print(f"Data successfully written to {output_file}")
