<script setup></script>

<template>
  <div
    class="my-16 max-w-screen-xl mx-auto flex flex-col lg:flex-row justify-center md:gap-8 gap-4 px-8"
  >
    <div
      class="w-full lg:w-2/3 shadow-lg bg-gray-200 mb-4 p-4 py-32 rounded flex flex-col justify-center"
    >
      <h1 class="text-slight-black text-2xl sm:text-4xl px-4 py-8 text-center">
        <b>asdasd</b> - ваш умный финансовый помощник
      </h1>

      <p class="text-slight-black text-lg sm:text-xl px-4 py-8 text-center">
        Используйте наш финансовый помощник, который объединяет удобство управления деньгами и мощь
        искусственного интеллекта. Наш сервис создан для тех, кто ценит контроль над своими
        финансами и время. С помощью <b>asdasd</b> вы можете легко управлять своими денежными
        средствами, отслеживать доходы и расходы, а также планировать бюджет на будущее.
      </p>
    </div>

    <div class="w-full lg:w-1/3 flex-col sm:flex-row lg:flex-col flex mb-4 gap-8">
      <div class="w-full bg-gray-200 shadow-lg h-full rounded flex flex-col items-center">
        <div class="text-slight-black px-4 py-8 text-center flex flex-col gap-3">
          <h1 class="text-lg md:text-2xl sm:text-xl font-bold hover:underline cursor-pointer">
            Помощник
          </h1>
          <p class="md:text-md text-sm">Лисёнок, помогающий с финансами</p>
        </div>

        <img src="/fox.png" alt="home" class="md:w-64 md:h-64 sm:w-48 sm:h-48 object-cover" />
      </div>

      <div class="w-full bg-gray-200 shadow-lg h-full rounded flex flex-col items-center">
        <div class="text-slight-black px-4 py-8 text-center flex flex-col gap-3">
          <h1 class="text-lg md:text-2xl font-bold hover:underline cursor-pointer">Кошелёк</h1>
          <p class="md:text-md text-sm">Удобное управление деньгами</p>
        </div>

        <img src="/wallet.png" alt="home" class="md:w-64 md:h-64 sm:w-48 sm:h-48 object-cover" />
      </div>
    </div>
  </div>
</template>
