import { category } from "./Data/Category.js";
import { expenses } from "./Data/Expenses.js";
import { expenseTags } from "./Data/Expenses Tags.js";
import "https://cdn.jsdelivr.net/npm/dayjs@1.11.19/dayjs.min.js";

const tagsList = []
function renderAddingExpenses() {
    const expenses_details = document.querySelector('.add-expenses-details');
    expenses_details.innerHTML = ` <div class="expense">
            <input type="number"name="Amount-input" placeholder="Enter: Amount you spent"class="inputs" data-type="amount-input">
            <label for="category-selector">Category: </label> 
            <select name="category-selector" class="inputs js-category-selector"data-type="category-input">   
            ${renderCategoryPane()}
            </select>
                </div>
                <div class="set-time">
                    <input type="checkbox"class="inputs inp-time-checkbox"name="time-checkbox"data-type = "timeanddate-input">
                    <label for="time-checkbox">Use The Current Date & Time?</label>
                <div class="inp-time-custom">
                <input type="date" class="inp-date"name="select-date">
                    <input type="time" class="inp-time"name="select-time">
                    <label for="select-date-time">Enter The Custom Date and Time Here</label>
                    </div>
                <div class="payment-method">
                    <select name="payment-mode" class = "inputs" data-type = "paymentmode-input">
                        <option selected value="online">Online Payment</option>
                        <option value="Offline">Ofline Payment</option>
                    </select>
                </div>
                <div class="tags">
                    <div class="added-tags">
                        Tags: []
                        </div>
                    <span class="tags-message"></span>
                    <div class="add-tags-list"></div>
                </div>
                <div class="comment">
                    <textarea name="comments-box" class="inputs comments-box" cols="20" rows="2" data-type = "comment-input"></textarea>
                    <label for="comments-box">Any Notes for Future You?. Regret, Was it Worth it... </label>
                </div>
                <button class="add-expense">Add Expense</button>
            </div>
            </div>`;
};

function renderCategoryPane() {
    let html = '';
    category.forEach(type => {
        html += `<option value="${type}">${type}</option>`
    })
    return html;
}
renderAddingExpenses();
addCustomTime();
renderTagsList(expenseTags);
addTagsEventListeners();
function addCustomTime() {
    let html;
    const checkbox = document.querySelector('.inp-time-checkbox');
    const customInp = document.querySelector('.inp-time-custom')
    checkbox.addEventListener('click', () => {
        if (checkbox.checked) {
            html = '';
        }
        else {
            html = `<input type="date" class="inp-date"name="select-date">
                    <input type="time" class="inp-time"name="select-time">
                    <label for="select-time select-time">Enter The Custom Date and Time Here</label>`;
        }
        customInp.innerHTML = html;
    })
}

function renderTagsList(list) {
    const tagsGrid = document.querySelector('.add-tags-list');
    let html = ''
    list.forEach(tag => {
        html += `<button class = "tag-buttons">${tag}</button>`;
    })
    tagsGrid.innerHTML = html;
}
function addTagsEventListeners() {
    const tagButtons = document.querySelectorAll('.tag-buttons')
    tagButtons.forEach(button => {
        button.addEventListener('click', () => {
            addToTagList(button.innerText);
        })
    })
}

function addToTagList(tag) {
    const tagsFullMessage = document.querySelector('.tags-message');
    let list = new Map();
    tagsList.forEach(item => {
        list.set(item)
    });
    if (list.has(tag)) {
        deleteTagList(tag);
        list.delete(tag);
        renderTags();
    }
    else if (tagsList.length < 4) {
        list.set(tag);
        tagsList.push(tag);
        renderTags();
    }
    else {
        tagsFullMessage.innerText = 'Cannot Add More Than 4 Tags'
    }
};

function renderTags() {
    const addedtags = document.querySelector('.added-tags');
    addedtags.innerHTML = `Tags: [${tagsList}]`
};

function deleteTagList(tag) {
    tagsList.splice(tagsList.indexOf(tag), 1);
};

function getValuesOfInput() {
    const inputs = document.querySelectorAll('.inputs');
    const result = {
        id: crypto.randomUUID(),
    }
    inputs.forEach(input => {
        let data = input.dataset.type;
        if (data === 'amount-input') {
            result.amount = input.value;
        }
        else if (data === 'category-input') {
            result.category = input.value;
        }
        else if (data === 'timeanddate-input') {
            if(input.checked){
                result.date = dayjs().format('DD MM YYYY');
                result.time = dayjs().format('HH:mm');
            }
            else{
                const date = document.querySelector('.inp-date').value;
                const time = document.querySelector('.inp-time').value;
                result.date = dayjs(date).format('DD MM YYYY');
                result.time = time;
            }
        }
        else if(data==='paymentmode-input'){
            result.paymentMode = input.value;
        }
        else if(data==='comment-input'){
            result.comment = input.value;
        };
        result.tags=tagsList;
    });
    console.log(result);
    

}

const addButton = document.querySelector('.add-expense');
addButton.addEventListener('click', () => {
    getValuesOfInput();
})