const url = window.location.href;
const checkBtn = document.querySelector('#check_btn');
const hide_search_form = document.querySelector('#hide_search_form');
// const save_visitor_form = document.querySelector('#save_visitor_form');
const searchForm = document.querySelector('#search-form');
const resultBox = document.querySelector('#result-box');
// const verifyBtn = document.getElementById('#verify-cont');

const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;





            function sendData(idnumber){
                $.ajax({
                    type: 'POST',
                    url: '/reception/check/',


                    data: {
                    'csrfmiddlewaretoken': csrf,
                    'id_number': idnumber
                     },

                  
                    success: (data) => {
                        if (Array.isArray(data)){
                            $("#modal-form").modal("show");
                            data.forEach(data => {
                              resultBox.innerHTML +=`
                    
                            <div class="mb-3">
                             <input type="text" class="form-control" hidden name="id_number" id="id_number" disabled value="${data.NIN}">
                           </div>
                              <div class="mb-3">
                                  <label>First name</label>
                                   <input type="text" class="form-control" name="first_name" id="first_name" disabled value="${data.FirstName}">
                                </div>
                    
                                <div class="mb-3">
                                <label>Middle name</label>
                                 <input type="text" class="form-control" name="middle_name" id="middle_name" disabled value="${data.MiddleName}">
                                </div>
                    
                                <div class="mb-3">
                                <label>Last name</label>
                                 <input type="text" class="form-control" name="last_name" id="last_name" disabled value="${data.LastName}">
                                </div>
                    
                                <div class="mb-3">
                                <label>Date of birth</label>
                                 <input type="text" class="form-control" name="date_of_birth" id="date_of_birth" disabled value="${data.DateofBirth}">
                                </div>
                    
                                <div class="mb-3">
                                <label>Gender</label>
                                 <input type="text" class="form-control" name="gender" id="gender" disabled value="${data.Sex}" >
                                </div>
                    
                                <div class="mb-3">
                                <label>On behalf (optional)</label>
                                 <input type="text" class="form-control" name="on_behalf" id="on_behalf">
                                </div>
                    
                                <div class="" id="verify-cont">
                                  <button id="verify_bt" class="btn bg-gradient-info w-100 mt-4 mb-0">Verify</button>
                                </div> 
                                `
                            });
                            
                           }else{
                            $("#modal-form").modal("show");
                            if (data == 'No data match!'){
                              resultBox.innerHTML = `<b>${data}</b>`
                              // alert(data)
                            }
                           }
                        
                    }

                });
            }
              
                


            var barcode = '';
            var interval;

        
            var barcode = '';
            var interval;
            document.addEventListener('keydown', function(evt) {
                if (interval)
                    clearInterval(interval);
                if (evt.code == 'Enter') {
                    if (barcode)
                        handleBarcode(barcode);
                    barcode = '';
                    return;
                }
                if (evt.key != 'Shift')
                    barcode += evt.key;
                interval = setInterval(() => barcode = '', 20);
            });

            function handleBarcode(scanned_barcode) {
                if (resultBox.classList.contains('not-visible')){
                    resultBox.classList.remove('not-visible')
                }
                document.querySelector('#last-barcode').value = scanned_barcode;
                sendData(scanned_barcode)

              
               
            }
    
