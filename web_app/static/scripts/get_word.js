$(document).ready(function() {
    // Add click event listener to words in the allWords textarea
    $('#allWords').on('click', 'span.wordtext', function() {
        var word = $(this).text(); // Get the clicked word
        // Send an AJAX request to fetch the meaning and part of speech for the clicked word
        $.ajax({
            url: '/get_word_details',
            method: 'POST',
            data: { word: word },
            success: function(response) {
                // Update the search result textarea with the meaning and part of speech
                $('#searchResult').val(response.meaning + ' - ' + response.part_of_speech);
            },
            error: function() {
                alert('Error fetching word details.');
            }
        });
    });
});