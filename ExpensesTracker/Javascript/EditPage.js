import { expenses } from "./Data/Expenses.js";

function renderExpenses(){
    const expenses_summary = document.querySelector('.expenses-summary');
    let html = '';
    expenses.forEach(log=>{
        html+=`<div class="expenses"></div>`;
    })
    expenses_summary.innerHTML = html;
}