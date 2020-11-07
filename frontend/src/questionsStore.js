const possibleQuestions = [
    {
        text: "How are you feeling currently?",
        type: "choice",
        answers:
            [{
                'id': 1,
                'text': 'I am feeling really great!'
            },
                {
                    'id': 2,
                    'text': 'I am feeling ok'
                }
            ]
    },
    {
        text: "How hard is it from 1 to 10 to do not use drugs on one day?",
        type: "slider",
        min: 0,
        step: 1,
        max: 10
    },
    {
        text: "How hard is it from 1 to 10 to do not use drugs on one day?",
        type: "multiple-choice",
        answers:
            [{
                'id': 1,
                'text': 'I am feeling really great!'
            },
                {
                    'id': 2,
                    'text': 'I am feeling ok'
                }
            ]
    }
]

export default {

    getNewQuestion: function () {
        let idx = Math.floor(Math.random() * possibleQuestions.length)
        return possibleQuestions[idx]
    }

}