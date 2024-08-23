class Node{
    constructor(data){
        this.data = data
        this.next = null
    }
}

class Linked_list{
    constructor(){
        this.root = null
        this.size = 0
    }

    insert(data, index=0){
        if (this.root == null){
            this.root = new Node(data)
        }else if(index == 0 || index == 1){
            let p = this.root
            while(p.next){
                p = p.next
            }
            p.next = new Node(data)
        }else{
            if (index > this.size + 1){
                console.log("Erro, não pode colocar valor em posição maior que a lista.")
            }else{
                node = new Node(data)
                p = p.next
                for(let c = 1; c < index; c++){
                    p = p.next
                }
                node.next = p.next
                p.next = node
            }
            
        }
        this.size += 1
    }

    deleta(index){
        if(this.root == null){
            console.log("A lista não tem nenhum valor, ['Adicione valor nela']")
        }else{
            if (index > this.size){
                console.log("Esse, numero é maior que a lista por favor, tente novamente!")
            }else if(index == 0 || index == 1){
                this.root = this.root.next
            }else{
                let a = this.root
                let p = this.root.next
                for(let c = 2; c < index; c++){
                    a = p
                    p = p.next
                }
                a.next = p.next
                p = p.next
            }
        }
    }

    replace_elemet(index, data){
        if (this.root == null){
            console.log("A lista esta vazia, adicione valor nela!")
        }else{
            let p = this.root 
            for (let c = 1; c < index; c++){
                p = p.next
            }
            p.data = data
        }
    }

    see_element_for_the_position(index){
        if(this.root == null){
            console.log("A Lista esta vazia, por favor adicione item nela")
        }else{
            if (index > this.size){
                console.log("Valor, não encontrado!")
            }else{
                let p = this.root
                for(let c = 1; c < index; c++){
                    p = p.next  
                }
                return console.log(p.data)
            }
        }
    }

    size_of_the_list(){
        let p = this.root
        let tmn = 0
        while(p){
            tmn += 1
            p = p.next
        }
        return console.log(tmn)
    }

    printar_tela(){
        let p = this.root
        while(p){
            console.log(p.data)
            p = p.next
        }
    }
}


var a = new Linked_list()
a.insert(100)
a.insert(2)
a.insert(3)
a.insert(4)
a.insert(22)
a.size_of_the_list()

