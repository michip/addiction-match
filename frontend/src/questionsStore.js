const possibleQuestions = [
    {
        text: "How are you feeling currently?",
        style: "radio",
        pk: 1,
        answers:
            [{
                'pk': 1,
                'value': 'I am feeling really great!'
            },
                {
                    'pk': 2,
                    'value': 'I am feeling ok'
                }
            ],
        selected: []
    },
    {
        text: "How hard is it from 1 to 10 to do not use drugs on one day?",
        type: "slider",
        pk: 2,
        min: 0,
        step: 1,
        max: 10
    },
    {
        text: "How hard is it from 1 to 10 to do not use drugs on one day?",
        type: "multiple-choice",
        pk: 3,
        answers:
            [{
                'pk': 1,
                'value': 'I am feeling really great!'
            },
                {
                    'pk': 2,
                    'value': 'I am feeling ok'
                }
            ]
    }
]

export default {

    getNewQuestion: function () {
        let pkx = Math.floor(Math.random() * possibleQuestions.length)
        return possibleQuestions[pkx]
    }

}