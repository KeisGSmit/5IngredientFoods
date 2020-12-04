$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.slider').slider();
    $('select').formSelect();
    $('.modal').modal();

    // Function to dynamically add input fields for "Instructions" and "Ingredients"
    //https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery
	let max_fields_instructions	  = 50; //maximum input boxes allowed for instructions
	let instructions_input_fields = $(".instructions_input_fields"); //Fields wrapper
	let add_button_instructions    = $(".add_field_instructions"); //Add button ID
    let instructions_count               = 1; //initlal text box count
    
    $(add_button_instructions).click(function(page){ //on add input button click
		page.preventDefault();
		if(instructions_count < max_fields_instructions){ //max input box allowed
            instructions_count++; //text box increment
            //add input box
			$(instructions_input_fields).append('<div><input name="instructions" type="text" class="validate" required><a href="#" class="btn-small background-color-secondary-2-1 remove_field">Remove</a></div>');
		}
	});
	
	$(instructions_input_fields).on("click",".remove_field", function(e){ //user click on remove text
		e.preventDefault(); $(this).parent('div').remove(); instructions_count--;
    });
    
    let max_fields_ingredients  	= 50; //maximum input boxes allowed for ingredients
    let ingredients_input_fields    = $(".ingredients_input_fields");
    let add_button_ingredients      = $(".add_field_ingredients");
    let ingredients_count          = 1;

	$(add_button_ingredients).click(function(page){
        page.preventDefault();
        if(ingredients_count < max_fields_ingredients){
            ingredients_count++;
            $(ingredients_input_fields).append('<div><input name="ingredients" type="text" class="validate" required><a href="#" class="btn-small background-color-secondary-2-1 remove_field">Remove</a></div>');
        }
    });

    $(ingredients_input_fields).on("click", ".remove_field", function(e){
        e.preventDefault(); $(this).parent('div').remove(); ingredients_count--;
    });

    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
});