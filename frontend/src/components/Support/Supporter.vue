<script setup>
import Wallet from '@/components/Support/WalletInSupport.vue';
import {ref} from 'vue'

const transactions = ref([
    {
        name:"wwwww",
        amount: '10100',
        currency: "руб.",
    },
    {
        name:"wwwww",
        amount: '10200',
        currency: "руб.",
    },{
        name:"wwwww",
        amount: '10300',
        currency: "руб.",
    },{
        name:"wwwww",
        amount: '10400',
        currency: "руб.",
    },{
        name:"wwwww",
        amount: '10500',
        currency: "руб.",
    },{
        name:"wwwww",
        amount: '10600',
        currency: "руб.",
    },
])

</script>

<template>
        <div class=" bg-slight-gray gap-10 lg:my-32 my-8 max-w-screen-xl mx-auto flex lg:flex-row flex-col justify-center px-4">
        <div class="lg:w-1/3">
                <div>
                    <p class="text-3xl font-bold text-slight-black text-center mb-10">Текущие кошельки</p>
                    <div>
                        <div class="rounded-lg max-h-96 w-full p-0 overflow-y-auto flex flex-col mb-2 scrollbar-none">
                            <div
                                class="flex flex-col w-full min-h-20 h-full rounded-xl justify-between items-center my-1"
                            >
                                <Wallet
                                v-for="transaction in transactions"
                                key="index"
                                class="my-2"
                                :name="transaction.name"
                                :amount="transaction.amount"
                                :currency="transaction.currency"
                                />
                            </div>
                        </div>
                    </div>
                </div>

        </div>
        <div class="lg:w-2/3 w-full md:gap-10 sm:gap-2 gap-10 flex sm:flex-row flex-col">
            <div class="lg:w-1/2 sm:order-1 order-2 ">
            <p class="text-3xl font-bold text-slight-black text-center mb-10">
                Советы от Лисёнка
            </p>
            <div class=" bg-gray-200 shadow h-full rounded overflow-y-auto scrollbar max-h-96">
                <p class="text-base text-slight-black sm:p-5 p-2">
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Est, illum, porro, unde dicta beatae neque quod eaque assumenda eos doloremque eum cumque vero ab? Animi ab possimus fuga exercitationem nihil necessitatibus ipsam ipsum repellat incidunt consequatur, autem nobis delectus excepturi maiores? Maiores blanditiis, quis, harum cupiditate, sint sequi est voluptatum provident labore quos error modi corrupti? Quis accusantium, molestiae illo ullam aut reprehenderit dolorem nemo at id nulla debitis alias, explicabo saepe excepturi! Aperiam amet quas quae quidem repellendus nesciunt quod et natus eum tempore perferendis quos, perspiciatis temporibus non molestias suscipit explicabo debitis facilis est aliquam distinctio odit praesentium. Suscipit, qui voluptas. Adipisci sit consectetur velit ipsum necessitatibus, dignissimos aperiam doloribus molestiae. Pariatur veniam sit minima dicta corrupti ipsam magni inventore error corporis reprehenderit aliquid assumenda a, minus laudantium dolores id eveniet vel magnam suscipit voluptatibus. Quisquam, asperiores. Iure magnam dicta laudantium necessitatibus eveniet. Officiis perspiciatis vero necessitatibus corporis ducimus. Tenetur nam repellat nostrum amet ipsa voluptas, numquam vel nesciunt provident possimus totam tempora, consequuntur enim accusamus hic quam, ullam perspiciatis mollitia quod in eos ipsam maiores assumenda? Libero, nobis alias aliquam excepturi commodi cupiditate saepe incidunt eos? Modi quae commodi debitis nostrum veniam, saepe voluptatum culpa assumenda libero, neque officiis quo dolore nisi fugit quis tenetur harum obcaecati quam ab temporibus. Incidunt error molestiae animi quia odio repudiandae enim tempora deserunt ducimus, aliquam dicta? Mollitia, consectetur. Dolores, corporis quaerat facere minus quae commodi eius dolor quia rerum nostrum. Quos vero quo fuga nostrum quas voluptate soluta vel nisi iusto dolorem natus deserunt eaque adipisci, autem, voluptates labore deleniti ipsam voluptas! Animi adipisci, quis sapiente quisquam mollitia, quaerat corporis voluptas totam itaque assumenda, aliquam eveniet quasi impedit exercitationem. At optio autem nam laudantium natus incidunt magnam quis in impedit, rem inventore eos ratione sunt iusto quia hic fuga dicta quidem facere ipsam. Adipisci repellendus dicta enim esse odio fugit provident voluptatem, a earum veniam harum id explicabo ad, molestias neque suscipit illum. Explicabo eaque ullam maxime et nihil quia, atque error iusto iure non totam recusandae expedita exercitationem, neque maiores delectus mollitia ipsa praesentium illo velit aperiam. Id saepe a minima nisi inventore numquam, obcaecati debitis impedit quas ratione culpa asperiores. Temporibus, at fugiat molestiae quo reprehenderit error reiciendis. Minima quia dignissimos at aut, culpa molestias rerum neque ea sequi enim aliquam possimus quidem totam nobis.
                </p>
            </div>
        </div>
        <div class="lg:w-1/2 sm:w-full sm:order-2 order-1 flex flex-col">
            <p class="text-3xl font-bold text-slight-black text-center mb-10 " >
                Дата и время
            </p>
            <div class="bg-gray-200 p-2 sm:p-10 rounded shadow flex flex-col gap-5 items-center justify-center">
                <div class=" bg-gray-300 shadow-lg h-full rounded p-1 sm:p-5">
                    <p class="text-bold text-center">От...</p>
                    <input class="rounded text-center" type="date"></input>
                </div>
                <div class="bg-gray-300  00 shadow-lg h-full rounded p-1 sm:p-5">
                    <p class="text-bold text-center">До...</p>
                    <input class="rounded text-center" type="date"></input>
                </div>
            </div>
            <button class="text-xl mt-10 bg-primary-yellow hover:bg-yellow-500 h-16 rounded-b shadow"> Скачать </button>
        </div>
        </div>
        
    </div>
</template>