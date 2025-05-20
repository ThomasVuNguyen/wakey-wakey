# Get predictions for individual WAV files (16-bit 16khz PCM)
from openwakeword.model import Model
model = Model(
    wakeword_models=["hey_jarvis_v0.1.tflite"],  # can also leave this argument empty to load all of the included pre-trained models
)
prediction = model.predict_clip("audio/2.wav")

print(prediction)

# Result: 10% is a good threshold