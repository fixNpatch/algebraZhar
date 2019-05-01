function run() {

    webix.ui({
        rows:[
            {/**spacer**/height:1},
            {
                rows:[
                    {
                        cols: [
                            {
                                gravity: 4,
                                view:"template",
                                type:"header",
                                template:"Автоключ Виженера",
                                tip: 'Составить таблицу'
                            },
                        ]
                    },
                ]
            },
            {/**spacer**/height:10},
            {
                cols:[
                    {/**spacer**/width:20},
                    {
                        id: 'resulted_text',
                        view: "textarea",
                        height: 540,
                        width:660,
                        on:{
                            'onChange': function(id){
                                // webix.message("Text loaded");
                            }
                        },
                    },
                    {/**spacer**/width:10},
                    {
                        rows:[
                            {
                                view:"button",
                                id:"open_button",
                                label:"Open",
                                inputWidth:100,
                                on:{
                                    'onItemClick': function(id){
                                        external.invoke('open');
                                    }
                                }
                            },
                            {
                                view:"button",
                                id:"save_button",
                                label:"Save",
                                inputWidth:100,
                                on:{
                                    'onItemClick': function(id){
                                        external.invoke('save');
                                    }
                                }
                            },
                            {
                                view:"button",
                                id:"clear_button",
                                label:"Clear",
                                inputWidth:100,
                                on:{
                                    'onItemClick': function(id){
                                        $$('resulted_text').define({value: ""});
                                        $$('resulted_text').refresh();
                                    }
                                }
                            },
                            {
                                view:"button",
                                id:"crypt_button",
                                label:"Сrypt",
                                inputWidth:100,
                                on:{
                                    'onItemClick': function(id){
                                        let text = $$('resulted_text').getValue(),
                                            param = $$('key_char').getValue();

                                        if (param === "") {
                                            webix.message("enter character");
                                            return
                                        }
                                        if (text === "") {
                                            webix.message("enter text");
                                            return
                                        }
                                        external.invoke('push:' + param + ':' + text);
                                    }
                                }
                            },
                            {
                                view:"button",
                                id:"decrypt_button",
                                label:"DeСrypt",
                                inputWidth:100,
                                on:{
                                    'onItemClick': function(id){
                                        let text = $$('resulted_text').getValue(),
                                            param = $$('key_char').getValue();

                                        if (param === "") {
                                            webix.message("enter character");
                                            return
                                        }
                                        if (text === "") {
                                            webix.message("enter text");
                                            return
                                        }
                                        external.invoke('pull:' + param + ':' + text);
                                    }
                                }
                            },
                            {
                                view:"text",
                                id: "key_char",
                                height: 40,
                                inputAlign:"center",
                                attributes:{
                                    maxLength:1,
                                }
                            },
                        ],
                    },
                    {/**spacer**/width:20},
                ],
            },
        ],
    });
}



document.addEventListener("DOMContentLoaded", run);