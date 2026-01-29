import "https://cdn.jsdelivr.net/npm/dayjs@1.11.19/dayjs.min.js";

const today = dayjs();

function greet_user() {
    const week_day = today.format('dddd')
    const greet = document.querySelector('.greetings');
    let greetings = '';
    if (week_day === 'Saturday' || week_day === 'Sunday') {
        greetings = `Guess what its ${today.format('dddd')}! and Even Better its a Weekend YAY! `
    }
    else{
        greetings = `Today is a boring ${week_day}, Have a Good Day.`;
    }
    greet.innerText = greetings;
}
greet_user()


