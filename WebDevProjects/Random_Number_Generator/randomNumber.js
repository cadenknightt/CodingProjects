// Generates random number
const randomNumber = () => {
     // Get elements for number generator:
     const minInput = document.getElementById('minNumber');
     const maxInput = document.getElementById('maxNumber');
     const messageBox = document.querySelector('.messageBox');
     const result = document.getElementById('randomNumber');
     const container = document.querySelector('#gridContainerLayout .container');

     // Reset prevoius CSS:
     if (messageBox) {
          messageBox.textContent = "";
          messageBox.classList.remove('messageBoxVisible');
     }
     if (container) {
          container.classList.remove('containerUpdate', 'containerWarning');
     }

     // Get and clean values if not NULL:
     const minVal = minInput?.value.trim() ?? '';
     const maxVal = maxInput?.value.trim() ?? '';

     // If either MIN or MAX is empty:
     if (!minVal || !maxVal) {
          if (messageBox) {
               messageBox.textContent = "PLEASE ENTER BOTH VALUES";
               messageBox.classList.add('messageBoxVisible');
          }
          if (container) container.classList.add('containerWarning');
          if (result) result.style.opacity = "0";
          return;
     }

     // Convert input to numbers:
     const min = Number(minVal);
     const max = Number(maxVal);

     // If length of both MIN and MAX are greater than 99999:
     if (min > 99999 || max > 99999) {
          if (messageBox) {
               messageBox.textContent = "VALUES MUST BE SMALLER THAN '99,999'";
               messageBox.classList.add('messageBoxVisible');
          }
          if (container) container.classList.add('containerWarning');
          if (result) result.style.opacity = "0";
          return;
     }

     // If length of both MIN and MAX are less than -99999:
     if (min < -99999 || max < -99999) {
          if (messageBox) {
               messageBox.textContent = "VALUES MUST BE GREATER THAN '-99,999'";
               messageBox.classList.add('messageBoxVisible');
          }
          if (container) container.classList.add('containerWarning');
          if (result) result.style.opacity = "0";
          return;
     }

     // If MIN is smaller than MAX:
     if (min > max) {
          if (messageBox) {
               messageBox.textContent = `'${min}' MUST BE SMALLER THAN '${max}'`;
               messageBox.classList.add('messageBoxVisible');
          }
          if (container) container.classList.add('containerWarning');
          if (result) result.style.opacity = "0";
          return;
     }
     
     // If MIN and MAX are equal:
     if (min === max) {
          if (messageBox) {
               messageBox.textContent =  `'${min}' MUST NOT BE USED TWICE`;
               messageBox.classList.add('messageBoxVisible');
          }
          if (container) container.classList.add('containerWarning');
          if (result) result.style.opacity = "0";
          return;
     }

     // Run random number generator
     const randomNum = Math.floor(Math.random() * (max - min + 1)) + min;
     // Add thousands comma placeholder
     const formattedNum = new Intl.NumberFormat('en-US').format(randomNum);

     // If all checks are clear run these:
     if (result) {
          result.textContent = formattedNum;
          result.style.opacity = "1";
     }
     if (container) container.classList.add('containerUpdate');
};
