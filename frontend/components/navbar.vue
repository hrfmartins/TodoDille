<template>
  <div>
    <b-navbar class="navbar-class" toggleable="lg" type="dark">
      <b-navbar-brand class="navbar-logo" href="/">TodoDille</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item class="nav-item-page" href="lists">Lists</b-nav-item>
          <b-nav-item class="nav-item-page" href="#" disabled>Calendar</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">

          <b-nav-item-dropdown class="nav-item-login" right disabled>
            <!-- Using 'button-content' slot -->
            <template #button-content>
              <font-awesome-icon :icon="['fas', 'lock']"></font-awesome-icon>
              <em>Account</em>
            </template>
            <b-dropdown-item href="#">Login</b-dropdown-item>
            <b-dropdown-item href="#">Sign Up</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: 'dashboardNavbar'
}
</script>

<style scoped>
.navbar-class {
  max-height: 15vh;
  background: rgba(0, 87, 175, 0.32);
}

.navbar-logo {
  font-size: 2rem;
  font-family: "Arial Narrow";
}

.nav-item-page {
  font-size: 1.5rem;
}

.nav-item-login {
  font-size: 1.5rem;
  border-radius: 10px;
  padding-left: 10px;
  padding-right: 10px;
}
</style>
