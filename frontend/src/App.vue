<template>
  <div class="container">
    <h1>Notification System</h1>
    <div class="row">
      <div class="form-group">
        <label for="category">Category:</label>
        <select class="form-control select-category" id="category" v-model="category">
          <option disabled value="">Please select a category</option>
          <option v-for="option in options" :value="option">{{ option }}</option>
        </select>
      </div>
      <div class="form-group">
        <label for="message">Message:</label>
        <textarea class="form-control" id="message" v-model="message"></textarea>
      </div>
      <div>
        <button
          class="btn btn-primary button"
          :disabled="!category || !message"
          @click="sendNotification"
        >
          Send Notification
        </button>
      </div>
    </div>

    <h2>Log History</h2>
    <div class="row row-table">
      <div class="col-md-12">
        <table class="table">
          <thead>
            <tr>
              <th>User ID</th>
              <th>User Name</th>
              <th>Category</th>
              <th>Channel</th>
              <th>Message</th>
              <th>Timestamp</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="log in logs" :key="log.timestamp">
              <td>{{ log.user_id }}</td>
              <td>{{ log.user_name }}</td>
              <td>{{ log.category }}</td>
              <td>{{ log.channel }}</td>
              <td>{{ log.message }}</td>
              <td>{{ log.timestamp }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      category: '',
      message: '',
      options: ['Sports', 'Finance', 'Movies'],
      logs: []
    }
  },
  mounted() {
    this.getLogs()
  },
  methods: {
    sendNotification() {
      const data = {
        category: this.category,
        message: this.message
      }
      const url = 'http://localhost:5000/notification'
      axios
        .post(url, data)
        .then((response) => {
          console.log(response.data.message)
          this.getLogs()
        })
        .catch((error) => {
          console.error(error)
        })
        .finally(() => {
          ;(this.category = ''), (this.message = '')
        })
    },
    getLogs() {
      const url = 'http://localhost:5000/log'
      axios
        .get(url)
        .then((response) => {
          this.logs = response.data
        })
        .catch((error) => {
          console.error(error)
        })
    }
  }
}
</script>
