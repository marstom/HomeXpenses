<template>
<nav class="navbar navbar-expand-lg navbar-light" style="background-color: #e3f2fd;">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor03" aria-controls="navbarColor03" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarColor03">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item">
          <router-link tag='a' to='/' class="nav-link" active-class="active" exact>Home <span class="sr-only">(current)</span></router-link>
        </li>
        <li class="nav-item">
          <router-link tag='a' :to="{name: 'expenses_list'}" class="nav-link" active-class="active">Lista wydatków</router-link>
        </li>
        <li class="nav-item">
          <router-link tag='a' :to="{name: 'add_expense'}" class="nav-link" active-class="active">Dodaj Wydatek</router-link>
        </li>
      </ul>
      <form class="form-inline">
        <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-primary my-1 my-sm-0" type="submit">Search</button>
      </form>
    </div>
  </nav>
</template>