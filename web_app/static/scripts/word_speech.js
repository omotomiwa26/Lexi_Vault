let speech = new SpeechSynthesisUtterance();

// Get the list of available voices
let voices = window.speechSynthesis.getVoices();

document.querySelector("#audioBtn").addEventListener("click", () => {
    speech.text = document.querySelector("#wordInput").value;

    // Randomly select a voice
    let randomVoiceIndex = Math.floor(Math.random() * voices.length);
    speech.voice = voices[randomVoiceIndex];

    window.speechSynthesis.speak(speech);
});