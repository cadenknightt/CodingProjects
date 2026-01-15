// Generates random number
const randomNumber = () => {
     // Get elements for number generator:
     const minInput = document.getElementById('minNumber');
     const maxInput = document.getElementById('maxNumber');
     const messageBox = document.querySelector('.messageBox');
     const result = document.querySelector('#gridContainerLayout .randomNumber');
     const container = document.querySelector('#gridContainerLayout .container');
     const inputContainer = document.querySelector('.min_maxValues');

     // Reset prevoius CSS:
     if (messageBox) {
          messageBox.textContent = "";
          messageBox.classList.remove('messageBoxVisible');
     }
     if (container) container.classList.remove('containerUpdate', 'containerWarning');
     if (inputContainer) inputContainer.classList.remove('min_maxValuesWarning');
     if (result) result.classList.remove('randomNumberHidden');

     // Get and clean values if not NULL:
     const minVal = (minInput?.value || '').replace(/,/g, '').trim();
     const maxVal = (maxInput?.value || '').replace(/,/g, '').trim();

     // If either MIN or MAX is empty:
     if (!minVal || !maxVal) {
          if (messageBox) {
               messageBox.textContent = "PLEASE ENTER BOTH VALUES";
               messageBox.classList.add('messageBoxVisible');
          }
          if (container) container.classList.add('containerWarning');
          if (inputContainer) inputContainer.classList.add('min_maxValuesWarning');
          if (result) result.classList.add('randomNumberHidden');
          return;
     }

     // Convert input to numbers:
     const min = Number(minVal);
     const max = Number(maxVal);

     if (isNaN(min) || isNaN(max)) {
          if (messageBox) {
               messageBox.textContent = "VALUES MUST BE NUMBERS";
               messageBox.classList.add('messageBoxVisible');
          }
          if (container) container.classList.add('containerWarning');
          if (inputContainer) inputContainer.classList.add('min_maxValuesWarning');
          if (result) result.classList.add('randomNumberHidden');
          return;
     }

     // If length of both MIN and MAX are greater than 99999:
     if (min > 99999 || max > 99999) {
          if (messageBox) {
               messageBox.textContent = "VALUES MUST BE SMALLER THAN '99,999'";
               messageBox.classList.add('messageBoxVisible');
          }
          if (container) container.classList.add('containerWarning');
          if (inputContainer) inputContainer.classList.add('min_maxValuesWarning');
          if (result) result.classList.add('randomNumberHidden');
          return;
     }

     // If length of both MIN and MAX are less than -99999:
     if (min < -99999 || max < -99999) {
          if (messageBox) {
               messageBox.textContent = "VALUES MUST BE GREATER THAN '-99,999'";
               messageBox.classList.add('messageBoxVisible');
          }
          if (container) container.classList.add('containerWarning');
          if (inputContainer) inputContainer.classList.add('min_maxValuesWarning');
          if (result) result.classList.add('randomNumberHidden');
          return;
     }

     // If MIN is smaller than MAX:
     if (min > max) {
          if (messageBox) {
               messageBox.textContent = `CHANGE '${min}' TO A NUMBER SMALLER THAN '${max}'`;
               messageBox.classList.add('messageBoxVisible');
          }
          if (container) container.classList.add('containerWarning');
          if (inputContainer) inputContainer.classList.add('min_maxValuesWarning');
          if (result) result.classList.add('randomNumberHidden');
          return;
     }
     
     // If MIN and MAX are equal:
     if (min === max) {
          if (messageBox) {
               messageBox.textContent =  `'${min}' MUST NOT BE USED TWICE`;
               messageBox.classList.add('messageBoxVisible');
          }
          if (container) container.classList.add('containerWarning');
          if (inputContainer) inputContainer.classList.add('min_maxValuesWarning');
          if (result) result.classList.add('randomNumberHidden');
          return;
     }

     // Run random number generator
     const randomNum = Math.floor(Math.random() * (max - min + 1)) + min;
     // Add thousands comma placeholder
     const formattedNum = new Intl.NumberFormat('en-US').format(randomNum);

     // If all checks are clear run these:
     if (result) {
          result.textContent = formattedNum;
          result.classList.add('randomNumber');
     }
     if (container) container.classList.add('containerUpdate');
};

// Add Cleave.js formatting for the input to use thousand places
document.addEventListener('DOMContentLoaded', () => {
    new Cleave('#minNumber', {
        numeral: true,
        numeralThousandsGroupStyle: 'thousand',
        numeralPositiveOnly: false,
        numeralDecimalScale: 0,
    });

    new Cleave('#maxNumber', {
        numeral: true,
        numeralThousandsGroupStyle: 'thousand',
        numeralPositiveOnly: false,
        numeralDecimalScale: 0,
    });
});
