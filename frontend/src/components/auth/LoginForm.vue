<template>
  <ValidationObserver ref="obs1" v-slot="{ invalid, validated }">
    <v-container class="fill-height" fluid>
      <img
        class="mx-auto mt-12"
        alt="Vue logo"
        src="../../assets/logo.png"
        width="107"
        height="72"
      />
      <v-row align="center" justify="center" class="mt-12">
        <v-col cols="12" sm="8" md="4">
          <v-card class="elevation-12 pb-8">
            <v-toolbar color="primary" dark flat>
              <v-toolbar-title>Login form</v-toolbar-title>
              <v-spacer></v-spacer>
            </v-toolbar>
            <v-card-text>
              <v-form @keyup.native.enter="onSubmit()">
                <ValidationProvider
                  name="username"
                  rules="required"
                  v-slot="{ errors, valid }"
                >
                  <v-text-field
                    label="Username"
                    v-model="username"
                    :error-messages="errors"
                    :success="valid"
                    required
                  />
                </ValidationProvider>

                <ValidationProvider
                  name="password"
                  rules="required"
                  v-slot="{ errors, valid }"
                >
                  <v-text-field
                    label="Password"
                    v-model="password"
                    :error-messages="errors"
                    :success="valid"
                    :type="show ? 'text' : 'password'"
                    :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                    clearable
                    required
                    @click:append="show = !show"
                  />
                </ValidationProvider>
                <v-btn
                  class="float-right"
                  @click="onSubmit()"
                  color="primary"
                  :disabled="invalid || !validated"
                  >Login</v-btn
                >
              </v-form>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </ValidationObserver>
</template>

<script>
import { ValidationObserver, ValidationProvider } from "vee-validate";
import { mapActions } from "vuex";
export default {
  components: {
    ValidationProvider,
    ValidationObserver,
  },
  data() {
    return {
      username: "",
      password: "",
      show: false,
    };
  },
  methods: {
    ...mapActions({
      login: "auth/AUTH_REQUEST",
    }),
    onSubmit() {
      this.login({
        username: this.username,
        password: this.password,
      });
    },
  },
};
</script>

<style lang="css" scope>
.form-signin {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: auto;
}
.form-signin .checkbox {
  font-weight: 400;
}
.form-signin .form-control {
  position: relative;
  box-sizing: border-box;
  height: auto;
  padding: 10px;
  font-size: 16px;
}
.form-signin .form-control:focus {
  z-index: 2;
}
.form-signin input[type="text"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
</style>
