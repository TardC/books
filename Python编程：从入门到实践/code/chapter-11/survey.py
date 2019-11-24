class AnonymousSurvey():
    """Collect answers to anonymous surveys."""

    def __init__(self, question):
        """Store a question and prepare for storing answers."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the questionnaire."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single survey answer."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all collected responses."""
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)
