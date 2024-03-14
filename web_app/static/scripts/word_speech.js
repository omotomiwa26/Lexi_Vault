function pronounceWord() {
    var word = document.getElementById("wordInput").value;
    
    // Check if the browser supports the SpeechSynthesis API
    if ('speechSynthesis' in window) {
        // Create a new SpeechSynthesisUtterance object with the word to be pronounced
        var utterance = new SpeechSynthesisUtterance(word);
        
        // Set the language to English (or any desired language)
        utterance.lang = 'en-US';

        utterance.onerror = function(event) {
            console.error('Speech synthesis error:', event.error);
        };

        // Speak the word
        speechSynthesis.speak(utterance);
    } else {
        // If the browser doesn't support SpeechSynthesis API, provide a fallback or display an error message
        console.log("Text-to-speech is not supported in this browser.");
        // You can also display a message to the user indicating that their browser doesn't support text-to-speech
    }
}
