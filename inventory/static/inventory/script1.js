document.getElementById("add-new-btn").addEventListener("click", function () {
  document.querySelector("#add-new-product").style.display = "flex";
  console.log("add-new-btn clicked");
});

document.querySelector("#close1").addEventListener("click", function () {
  document.querySelector("#add-new-product").style.display = "none";
  console.log("close1 clicked");
});

// document.getElementById("update-btn").addEventListener("click", function() {
// 	document.querySelector("#update-product").style.display = "flex";
// 	console.log("update-btn clicked");
// });

// document.getElementById("delete-btn").addEventListener("click", function() {
// 	// document.querySelector(".bg-modal").style.display = "flex";
// 	console.log("delete-btn clicked");
// });

document.querySelector("#close2").addEventListener("click", function () {
  document.querySelector("#update-product").style.display = "none";
  console.log("close2 clicked");
});

//////////////////////////////////////////////////////////////////
$(document).ready(function () {
  BindProducts();
});


//this code adds data in both sqlite3 and elasticsearch 

$("#btnSubmit").click(function () {
  // let idValue = $('#txtId').val();
  let product_name = $("#product_name").val();
  let price = $("#price").val();
  let quantity = $("#quantity").val();

  $.ajax({
    type: "POST",
    dataType: "json",
    // dataType: "jsonp",
    // headers: {'X-CSRFToken': csrftoken},
    // headers: {
    //   "Access-Control-Allow-Origin": "*",
    //   "Access-Control-Allow-Methods": "GET, POST, DELETE, PUT",
    // },
    data: {
      product_name: product_name,
      price: price,
      quantity: quantity,
    },

    url: "http://localhost:8000/api/inventory/",
    // url: "http://localhost:9200/company/doc/",

    error: function (xhr, status, error) {
      var err_msg = "";
      for (var prop in xhr.responseJSON) {
        err_msg += prop + ": " + xhr.responseJSON[prop] + "\n";
      }

      alert(err_msg);
    },
    success: function (result) {
      BindProducts();
      // alert("Data Saved Successfully.");

      $("#product_name").val("");
      $("#price").val("");
      $("#quantity").val("");
    },
  });


  //elasticsearch test-xhr [can also be done via ajax]
  var data = JSON.stringify({
    "product_name": product_name,
    "price": price,
    "quantity": quantity,
  });

  console.log("data_before_sending", data);

  var xhr = new XMLHttpRequest();
  // xhr.withCredentials = true;
  var async = true;

  console.log("xhr_req", xhr);

  xhr.addEventListener("readystatechange", function () {
    if (this.readyState === 4) {
      console.log(this.responseText);
    }
  });

  xhr.open("POST", "http://localhost:9200/company/doc/", async);
  xhr.setRequestHeader("Content-Type", "application/json");
  // xhr.setRequestHeader("Access-Control-Allow-Origin", "*");
  // xhr.setRequestHeader("Access-Control-Allow-Methods", "*");
  // xhr.setRequestHeader("Access-Control-Allow-Headers", "*");

  xhr.send(data);

  document.querySelector("#add-new-product").style.display = "none";
});

function BindProducts() {
  //   let result;

  $.ajax({
    type: "GET",
    dataType: "json",
    url: "http://localhost:8000/api/inventory/",
    success: function (result) {
      //   console.log(result);

      var totalCount = result.length;
      var structureDiv = "";

      let test_variable = result;

      //to display latest added first
      for (let i = totalCount - 1; i >= 0; i--) {
        var new_object = {
          id: result[i].id,
          product_name: result[i].product_name,
          price: result[i].price,
          quantity: result[i].quantity,
        };

        // let test_variable = result[i];

        structureDiv +=
          "<tr>" +
          "	<th>" +
          result[i].id +
          "</th>" +
          "      <td>" +
          result[i].product_name +
          "</td>" +
          "             <td>" +
          result[i].price +
          "</td>" +
          "              <td>" +
          result[i].quantity +
          "</td>" +
          "              <td>" +
          result[i].date_posted +
          "</td>" +
          //   console.log(test_variable[i]) +

          //    console.log(new_object) +

          "<td class='text-center'>\
			<button type='button' class='btn btn-sm btn-primary' \
			onclick='update_func(" +
          new_object.id +
          ")'><span class='fa fa-pencil'></span></button>\
			<button type='button' class='btn btn-sm btn-danger' \
			onclick='delete_confirmation_func(" +
          result[i].id +
          ")'><span class='fa fa-trash'></span></button>\
		  </td>" +
          "           </tr>";
      }
      $("#divBody").html(structureDiv);
    },
  });
}

function DeleteRow(id) {
  $.ajax({
    type: "DELETE",
    dataType: "json",

    // DELETE FROM inventory_product WHERE id = id;

    url: "http://localhost:8000/api/inventory/" + id + "/",
    error: function (xhr, status, error) {
      var err_msg = "";
      for (var prop in xhr.responseJSON) {
        err_msg += prop + ": " + xhr.responseJSON[prop] + "\n";
      }

      alert(err_msg);
    },
    success: function (result) {
      BindProducts();
    },
  });
}

//to display update modal
function update_func(res) {
  console.log("result", res);

  document.querySelector("#update-product").style.display = "flex"; //to display popup

  // $("#product_name1").val(res.product_name);
  // $("#price1").val(res.price);
  // $("#quantity1").val(res.quantity);

  // console.log(res.id);

  // console.log(res);

  let id_to_pass = res;

  $("#update-btnSubmit").click(function () {
    console.log("update-btnSubmit clicked");

    console.log(id_to_pass);

    // let id = id;
    let product_name = $("#product_name1").val();
    let price = $("#price1").val();
    let quantity = $("#quantity1").val();

    $.ajax({
      type: "PUT",
      dataType: "json",
      // headers: {'X-CSRFToken': csrftoken},

      data: {
        product_name: product_name,
        price: price,
        quantity: quantity,
      },

      url: "http://localhost:8000/api/inventory/" + id_to_pass + "/",
      error: function (xhr, status, error) {
        var err_msg = "";
        for (var prop in xhr.responseJSON) {
          err_msg += prop + ": " + xhr.responseJSON[prop] + "\n";
        }

        alert(err_msg);
      },
      success: function (result) {
        BindProducts();
        alert("Data Saved Successfully.");
      },
    });

    //then hide the submit button
    document.querySelector("#update-product").style.display = "none";
  });

  console.log("update-btn clicked");
}

// function UpdateRow(id) {

// 	console.log("update-btnSubmit clicked");
// 	console.log(id_to_pass);

// 	// let id = id;
// 	let product_name = $("#product_name1").val();
// 	let price = $("#price1").val();
// 	let quantity = $("#quantity1").val();

// 	$.ajax({
// 	  type: "PUT",
// 	  dataType: "json",
// 	  headers: {'X-CSRFToken': csrftoken},

// 	  data: {
// 		product_name: product_name,
// 		price: price,
// 		quantity: quantity,
// 	  },

// 	  url: "http://localhost:8000/api/inventory/"+ id_to_pass +"/",
// 	  error: function (xhr, status, error) {
// 		var err_msg = "";
// 		for (var prop in xhr.responseJSON) {
// 		  err_msg += prop + ": " + xhr.responseJSON[prop] + "\n";
// 		}

// 		alert(err_msg);
// 	  },
// 	  success: function (result) {
// 		BindProducts();
// 		alert("Data Saved Successfully.");

// 		$("#product_name").val("");
// 		$("#price").val("");
// 		$("#quantity").val("");
// 	  },
// 	});
// };

function delete_confirmation_func(id) {
  var result = confirm("Want to delete?");

  console.log(result);
  if (result) {
    DeleteRow(id);
  }
}
