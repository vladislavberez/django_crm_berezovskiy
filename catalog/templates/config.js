CKEDITOR.editorConfig = function( config ) {

   //   config.enterMode = 2; //disabled <p> completely
        config.enterMode = CKEDITOR.ENTER_BR; // pressing the ENTER KEY input <br/>
        config.shiftEnterMode = CKEDITOR.ENTER_P; //pressing the SHIFT + ENTER KEYS input <p>
        config.autoParagraph = false; // stops automatic insertion of <p> on focus
    };