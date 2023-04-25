
const checkBtnScanner = document.querySelector('#check_btn');
const hide_search_formscanner = document.querySelector('#hide_search_form');
// const save_visitor_form = document.querySelector('#save_visitor_form');
const searchFormscanner = document.querySelector('#search-form');
const resultBoxscanner = document.querySelector('#result-box');
// const verifyBtn = document.getElementById('#verify-cont');

const csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;





            function sendData(idnumber){
                $.ajax({
                    type: 'POST',
                    url: '/customers/check/',


                    data: {
                    'csrfmiddlewaretoken': csrfToken,
                    'id_number': idnumber
                     },

                  
                    success: (res) => {
                        console.log(res.data)
                        if (Array.isArray(res.data)){
                            $("#modal-form").modal("show");
                            res.data.forEach(result=> {
                                resultBoxscanner.innerHTML +=`
                    
                            <div class="mb-3">
                             <input type="text" class="form-control" hidden name="id_number" id="id_number" disabled value="${res.data.NIN}">
                           </div>
                              <div class="mb-3">
                                  <label>First name</label>
                                   <input type="text" class="form-control" name="first_name" id="first_name" disabled value="${res.data.FirstName}">
                                </div>
                    
                                <div class="mb-3">
                                <label>Middle name</label>
                                 <input type="text" class="form-control" name="middle_name" id="middle_name" disabled value="${res.data.MiddleName}">
                                </div>
                    
                                <div class="mb-3">
                                <label>Last name</label>
                                 <input type="text" class="form-control" name="last_name" id="last_name" disabled value="${res.data.LastName}">
                                </div>
                    
                                <div class="mb-3">
                                <label>Date of birth</label>
                                 <input type="text" class="form-control" name="date_of_birth" id="date_of_birth" disabled value="${res.data.DateofBirth}">
                                </div>
                    
                                <div class="mb-3">
                                <label>Gender</label>
                                 <input type="text" class="form-control" name="gender" id="gender" disabled value="${res.data.Sex}" >
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
                            if (res.data == 'No data match!'){
                                resultBoxscanner.innerHTML = `<b>${res.data}</b>`
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
                if (resultBoxscanner.classList.contains('not-visible')){
                    resultBoxscanner.classList.remove('not-visible')
                }
                document.querySelector('#last-barcode').value = scanned_barcode;
                sendData(scanned_barcode)

              
               
            }
    
